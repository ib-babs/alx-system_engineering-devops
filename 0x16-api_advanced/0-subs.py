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

    subscribers = requests.get(url, allow_redirects=False)

    if subscribers.status_code == 200:
        return (subscribers.json()['data']['subscribers'])
    else:
        return (0)
