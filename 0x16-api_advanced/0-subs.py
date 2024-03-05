#!/usr/bin/python3
"""
Queries Reddit API & returns number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Parameters:
        subreddit (str): The subreddit to query.

    Returns:
        int: Number of subscribers for given subreddit
        or 0 if subreddit is invalid.
    """

    url = "https://www.reddit.com/r/{}/about.json"
    headers = {"User-Agent": "Custom"}
    response = requests.get(url.format(subreddit), headers=headers)

    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers', 0)
