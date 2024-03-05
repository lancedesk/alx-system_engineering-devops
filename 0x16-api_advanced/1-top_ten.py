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
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
