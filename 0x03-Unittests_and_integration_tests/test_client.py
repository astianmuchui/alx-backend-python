#!/usr/bin/env python3

"""
Test cases for client module
"""

from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized

GithubOrgClient = __import__('client').GithubOrgClient
get_json = __import__('utils').get_json


class TestGithubOrgClient(TestCase):
    """
    TestGithubOrgClient class
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        test_org method
        """
        test_payload = {"payload": True}
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org(), test_payload)
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_public_repos(self, org_name, mock_get_json):
        """
        test_public_repos method
        """
        test_payload = [{"name": "holberton"}]
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org_name)
        self.assertEqual(client.public_repos(), ["holberton"])
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_public_repos_with_license(self, org_name, mock_get_json):
        """
        test_public_repos_with_license method
        """
        test_payload = [{"name": "holberton", "license":
                         {"key": "my_license"}}]
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org_name)
        self.assertEqual(client.public_repos("my_license"), ["holberton"])
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_public_repos_with_license_none(self, org_name, mock_get_json):
        """
        test_public_repos_with_license_none method
        """
        test_payload = [{"name": "holberton", "license":
                         {"key": "my_license"}}]
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org_name)
        self.assertEqual(client.public_repos(None), ["holberton"])
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_public_repos_with_license_not_found(self, org_name,
                                                 mock_get_json):
        """
        test_public_repos_with_license_not_found method
        """
        test_payload = [{"name": "holberton", "license":
                         {"key": "my_license"}}]
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org_name)
        self.assertEqual(client.public_repos("not_found"), [])
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_public_repos_with_license_empty(self, org_name, mock_get_json):
        """
        test_public_repos_with_license_empty method
        """
        test_payload = [{"name": "holberton", "license":
                         {"key": ""}}]
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org_name)
        self.assertEqual(client.public_repos(""), [])
        mock_get_json.assert_called_once()
