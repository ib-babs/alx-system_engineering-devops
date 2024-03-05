#!/usr/bin/python3
"""Reddit API - Application Programming Interface
Get top 10 hot posts"""


import requests


def top_ten(subreddit):
    """Get the top 10 hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        "User-Agent": '0x16-api_advanced:project:\
v1.0.0 (by /u/drkhalil05)'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.jsons()
        titles = [r['data']['title'] for r in data['data']['children']]
        for r in titles:
            print(r)
    else:
        print(None)
