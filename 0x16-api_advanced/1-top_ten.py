#!/usr/bin/python3
"""
Queries Reddit API & prints titles of first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Parameters:
        subreddit (str): The subreddit to query.

    Returns:
        None
    """

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        print("None")
        return

    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
