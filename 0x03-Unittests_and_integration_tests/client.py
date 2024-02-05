#!/usr/bin/env python3
"""A GitHub org client."""
from typing import List, Dict
from utils import get_json, access_nested_map, memoize


class GithubOrgClient:
    """A GitHub org client."""

    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -> None:
        """Initialize the GithubOrgClient.

        Parameters:
            org_name (str): The name of the GitHub organization
        """
        self._org_name = org_name

    @memoize
    def org(self) -> Dict:
        """Memoized org."""
        return get_json(self.ORG_URL.format(org=self._org_name))

    @property
    def _public_repos_url(self) -> str:
        """Public repos URL."""
        return self.org["repos_url"]

    @memoize
    def repos_payload(self) -> Dict:
        """Memoized repos payload."""
        return get_json(self._public_repos_url)

    def public_repos(self, license: str = None) -> List[str]:
        """Retrieve public repos.

        Parameters:
            license (str): Filter repos by license (default: None)

        Returns:
            List[str]: List of public repos
        """
        json_payload = self.repos_payload
        public_repos = [
            repo["name"] for repo in json_payload
            if license is None or self.has_license(repo, license)
        ]

        return public_repos

    @staticmethod
    def has_license(repo: Dict[str, Dict], license_key: str) -> bool:
        """Check if a repository has a specific license.

        Parameters:
            repo (Dict[str, Dict]): The repository information
            license_key (str): The license key to check

        Returns:
            bool: True if the repository has the specified license, False otherwise
        """
        assert license_key is not None, "license_key cannot be None"
        try:
            has_license = access_nested_map(
                repo, ("license", "key")) == license_key
        except KeyError:
            return False
        return has_license
