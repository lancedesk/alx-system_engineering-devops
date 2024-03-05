#!/usr/bin/python3
"""
Recursively queries the Reddit API, parses the titles of all hot articles,
and prints a sorted count of given keywords.
"""
from requests import get
from sys import argv


def count_words(subreddit, word_list, after="", counter={}, t=0):
    """
    Parameters:
        subreddit (str): The subreddit to query.
        word_list (list): A list of keywords to count.
        after (str): A token for pagination in Reddit API.
        counter (dict): A dictionary to count keywords.

    Returns:
        None
    """
    if t == 0:
        for word in word_list:
            counter[word] = 0

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    json = get("https://api.reddit.com/r/{}/hot?after={}".
               format(subreddit, after), headers=headers).json()

    try:
        key = json['data']['after']
        data = json['data']['children']
        for obj in data:
            for word in counter:
                counter[word] += obj['data']['title'].lower().split(
                    ' ').count(word.lower())

        if key is not None:
            count_words(subreddit, word_list, key, counter, 1)

        else:
            posts = sorted(counter.items(), key=lambda i: i[1], reverse=True)
            for key, value in posts:
                if value != 0:
                    print('{}: {}'.format(key, value))
    except Exception:
        return None
