#!/usr/bin/python3
import requests
"""
Queries Reddit API & prints titles of first 10 hot posts
listed for a given subreddit.
"""


def top_ten(subreddit):
    """
    Parameters:
        subreddit (str): The subreddit to query.

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    payload = {"limit": "10"}
    response = requests.get(url, headers=headers, params=payload,
                            allow_redirects=False)
    if response.status_code != 200:
        print("None")
    else:
        hot_topics = response.json().get("data").get("children")
        titles = [post.get("data").get("title") for post in hot_topics]
        print(*titles, sep='\n')
