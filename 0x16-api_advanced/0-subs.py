#!/usr/bin/python3
""" Exporting csv files"""
import json
import requests
import sys


def number_of_subscribers(subreddit):
    """Read reddit API and return number subscribers """
    username = 'ledbag123'
    password = 'Reddit72'
    user_pass_dict = {'user': username, 'passwd': password, 'api_type': 'json'}
    headers = {'user-agent': '/u/ledbag123 API Python for Holberton School'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    client = requests.session()
    client.headers = headers
    r = client.get(url, allow_redirects=False)
    if r.status_code == 200:
        return (r.json()["data"]["subscribers"])
    else:
        return (0)
# #!/usr/bin/python3
# """Reddit API - Application Programming Interface
# Queries the Reddit API and returns the number of
# subscribers (not active users, total subscribers)
# for a given subreddit. If an invalid subreddit is given,
# the function should return 0."""

# import requests


# def number_of_subscribers(subreddit):
#     """Get the number of the REDDIT subscribers"""
#     url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

#     subscribers = requests.get(url, allow_redirects=False)

#     if subscribers.status_code == 200:
#         return (subscribers.json()['data']['subscribers'])
#     else:
#         return (0)
