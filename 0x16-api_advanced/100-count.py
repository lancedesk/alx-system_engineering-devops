#!/usr/bin/python3
"""
Recursively queries the Reddit API, parses the titles of all hot articles,
and prints a sorted count of given keywords.
"""
from requests import get


def count_words(subreddit, word_list, after=None, counter=None):
    """
    Parameters:
        subreddit (str): The subreddit to query.
        word_list (list): A list of keywords to count.
        after (str): A token for pagination in Reddit API.
        counter (dict): A dictionary to count keywords.

    Returns:
        None
    """
    if counter is None:
        counter = {}

    if after is None:
        headers = {"User-Agent": "Custom"}
        url = "https://api.reddit.com/r/{}/hot".format(subreddit)
    else:
        headers = {"User-Agent": "Custom", "after": after}
        reddit_url = "https://api.reddit.com/r/{}/hot?after={}"
        url = reddit_url.format(subreddit, after)

    response = get(url, headers=headers)
    if response.status_code != 200:
        print("An error occurred while querying the Reddit API.")
        return

    try:
        data = response.json()['data']
        after = data['after']
        children = data['children']

        # Count the occurrences of each word in the titles
        for child in children:
            title = child['data']['title'].lower()
            for word in word_list:
                if word.lower() in title.split():
                    counter[word.lower()] = counter.get(word.lower(), 0) + 1

        if after is not None:
            count_words(subreddit, word_list, after, counter)
        else:
            # Sort counter dictionary by count (descending) & word (ascending)
            sorted_cntr = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

            # Print the results
            for word, count in sorted_cntr:
                print("{}: {}".format(word, count))

    except KeyError:
        print("No data available for the given subreddit.")
        return


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'"
              .format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        keywords = sys.argv[2].split()
        count_words(subreddit, keywords)
