#!/usr/bin/python3
"""
To get a request of users in commit "rails"
"""

import requests
from sys import argv

if __name__ == "__main__":
    repo_name = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(repo_name, owner)
    headers = {
        'Accept': 'Accept: application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }

    response = requests.get(url)
    commits = response.json()
    try:
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print("{}: {}".format(sha, author_name))
    except IndexError:
        pass
