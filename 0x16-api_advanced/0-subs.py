#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0

    r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/drkhalil05)'})
    if r.status_code == 200:
        try:
            sub = r.json()
            result = sub.get('data').get('subscribers')
            if result is not None:
                return (result)
        except Exception as e:
            pass
    else:
        return 0
