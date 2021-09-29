#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
"""
import requests
import json


def number_of_subscribers(subreddit):
    """Funciton that returns the number of subscribers"""
    url = "https://api.reddit.com/r/{}/about.json".format(subreddit)
    head = {"User-Agent": "Client"}
    request = requests.get(url, headers=head)
    if request.status_code != 200:
        return 0
    response = json.loads(request.text)
    data = response["data"]
    return data["subscribers"]
