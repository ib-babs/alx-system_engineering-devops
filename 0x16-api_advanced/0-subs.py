#!/usr/bin/python3
"""Reddit API - Application Programming Interface
Queries the Reddit API and returns the number of
subscribers (not active users, total subscribers)
for a given subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Get the number of the REDDIT subscribers"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        "User-Agent": '0x16-api_advanced:project:\
v1.0.0 (by /u/drkhalil05)'
    }
    subscribers = requests.get(url, headers=headers, allow_redirects=False)

    if subscribers.status_code == 200:
        return (subscribers.json()['data']['subscribers'])
    else:
        return (0)
