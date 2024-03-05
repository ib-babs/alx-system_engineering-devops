#!/usr/bin/python3
"""Reddit API - Application Programming Interface
Queries the Reddit API and returns the number of
subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given,
the function should return 0."""

import requests


def number_of_subscribers(subreddit):
    """Get the number of the REDDIT subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/96.0.4664.110 Safari/537.36"
    }

    subscribers = requests.get(url, headers=headers, allow_redirects=False)

    if subscribers.status_code == 200:
        json_result = subscribers.json()
        subscriber_counts = json_result.get('data')['subscribers']
        if subscriber_counts is not None:
            return (subscriber_counts)
    else:
        return (0)
