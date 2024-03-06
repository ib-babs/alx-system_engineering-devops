#!/usr/bin/python3
"""Reddit API - Application Programming Interface
Get top 10 hot posts"""


import requests


def top_ten(subreddit):
    """Get the top 10 hot posts"""
    if subreddit is None:
        return 0
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": '0x16-api_advanced:project:\
v1.0.0 (by /u/drkhalil05)'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()
            titles = [r['data']['title'] for r in data['data']['children']]
            for r in titles:
                print(r)
        except Exception as e:
            print(None)
    else:
        print(None)
