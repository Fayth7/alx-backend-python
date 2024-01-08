#!/usr/bin/env python3
"""A GitHub organization client."""

from typing import List, Dict
from utils import get_json, access_nested_map, memoize


class GithubOrgClient:
    """GitHub organization client."""

    API_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -> None:
        """Initialize GithubOrgClient."""
        self._org_name = org_name

    @property
    @memoize
    def org_info(self) -> Dict:
        """Memoized organization information."""
        return get_json(self.API_URL.format(org=self._org_name))

    @property
    def public_repos_url(self) -> str:
        """URL for public repositories."""
        return self.org_info.get("repos_url", "")

    @property
    @memoize
    def repos_payload(self) -> Dict:
        """Memoized repository payload."""
        return get_json(self.public_repos_url)

    def public_repos(self, license: str = None) -> List[str]:
        """List of public repositories, optionally filtered by license."""
        repos = self.repos_payload
        return [repo["name"] for repo in repos if not license
                or self.has_license(repo, license)]

    @staticmethod
    def has_license(repo: Dict[str, Dict], license_key: str) -> bool:
        """Check if a repository has a specified license."""
        return access_nested_map(repo, ("license", "key"), default="") == license_key


if __name__ == "__main__":
    # Example usage
    github_client = GithubOrgClient("example_org")
    print("Organization Info:", github_client.org_info)
    print("Public Repositories:", github_client.public_repos())
