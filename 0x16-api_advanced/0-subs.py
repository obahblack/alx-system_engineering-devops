#!/usr/bin/python3
"""
Query Reddit API for number of subscribers for a given su
"""
import sys
from requests import get

def number_of_subscribers(subreddit):
    """
    return number of subscribers for a given subreddit
    return 0 if invalid subreddit givven
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {'user-agent': 'my-app/0.0.1'}

    r = get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return 0

    try:
        js = r.json()

    except ValueError:
        return 0

    data = js.get("data")

    if data:
        sub_count = data.get("subscribers")
        if sub_count:
            return sub_count

    return 0
