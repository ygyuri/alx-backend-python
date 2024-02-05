#!/usr/bin/env python3
"""
Unit tests for client.GithubOrgClient class.
"""


import unittest
from unittest.mock import patch, Mock, PropertyMock, call
from parameterized import parameterized, parameterized_class
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrgClient class that inherits from unittest.TestCase.
    """

    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected, patch):
        """
        Test that GithubOrgClient.org returns the correct value.
        """
        patch.return_value = expected
        x = GithubOrgClient(org_name)
        self.assertEqual(x.org, expected)
        patch.assert_called_once_with("https://api.github.com/orgs/"+org_name)

    def test_public_repos_url(self):
        """
        Test the GithubOrgClient._public_repos_url property.
        """
        expected = "www.yes.com"
        payload = {"repos_url": expected}
        to_mock = 'client.GithubOrgClient.org'
        with patch(to_mock, PropertyMock(return_value=payload)):
            cli = GithubOrgClient("x")
            self.assertEqual(cli._public_repos_url, expected)

    @patch('client.get_json')
    def test_public_repos(self, get_json_mock):
        """
        Test the GithubOrgClient.public_repos method.
        """
        peter = {"name": "peter", "license": {"key": "a"}}
        keroti = {"name": "keroti", "license": {"key": "b"}}
        smith = {"name": "smith"}
        to_mock = 'client.GithubOrgClient._public_repos_url'
        get_json_mock.return_value = [peter, keroti, smith]
        with patch(to_mock, PropertyMock(return_value="www.yes.com")) as y:
            x = GithubOrgClient("x")
            self.assertEqual(x.public_repos(), ['peter', 'keroti', 'smith'])
            self.assertEqual(x.public_repos("a"), ['peter'])
            self.assertEqual(x.public_repos("c"), [])
            self.assertEqual(x.public_repos(45), [])
            get_json_mock.assert_called_once_with("www.yes.com")
            y.assert_called_once_with()

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])
    def test_has_license(self, repo, license, expected):
        """ test the license checker """
        self.assertEqual(GithubOrgClient.has_license(repo, license), expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration test for github org client """

    @classmethod
    def setUpClass(cls):
        """ prepare for testing """
        org = TEST_PAYLOAD[0][0]
        repos = TEST_PAYLOAD[0][1]
        org_mock = Mock()
        org_mock.json = Mock(return_value=org)
        cls.org_mock = org_mock
        repos_mock = Mock()
        repos_mock.json = Mock(return_value=repos)
        cls.repos_mock = repos_mock
        cls.get_patcher = patch('requests.get')
        cls.get = cls.get_patcher.start()
        options = {cls.org_payload["repos_url"]: repos_mock}
        cls.get.side_effect = lambda y: options.get(y, org_mock)

    @classmethod
    def tearDownClass(cls):
        """ unprepare for testing """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test public repos
        """
        self.mock_get.return_value.json.side_effect = [
            self.org_payload, self.repos_payload
        ]
        client = GithubOrgClient("test")
        expected_result = ["repo1", "repo2"]

        result = client.public_repos()

        self.assertEqual(result, expected_result)
        self.mock_get.assert_called_with(
            "https://api.github.com/orgs/test/repos"
        )

    def test_public_repos_with_license(self):
        """
        Test Public repos
        """
        self.mock_get.return_value.json.side_effect = [
            self.org_payload, self.repos_payload
        ]
        client = GithubOrgClient("test")
        expected_result = ["repo1"]

        result = client.public_repos("license_key")

        self.assertEqual(result, expected_result)
        self.mock_get.assert_called_with(
            "https://api.github.com/orgs/test/repos")
