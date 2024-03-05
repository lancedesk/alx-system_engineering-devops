#!/usr/bin/python3
"""
    Recursively queries the Reddit API, parses the titles of all hot articles,
    and prints a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Parameters:
        subreddit (str): The subreddit to query.
        word_list (list): A list of keywords to count.
        after (str): The Reddit post ID to start the query from.
        counts (dict): A dictionary to store the count of each keyword.

    Returns:
        None
    """
    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(None)
        return

    data = response.json().get('data', {})
    after = data.get('after', None)
    children = data.get('children', [])

    for child in children:
        title = child.get('data', {}).get('title', '').lower()
        for word in word_list:
            if title.count(word.lower()) > 0:
                counts[word] = counts.get(word, 0) + title.count(word.lower())

    if after is not None:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
