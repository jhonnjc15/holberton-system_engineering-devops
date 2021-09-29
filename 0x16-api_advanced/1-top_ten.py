#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """Prints the first 10 hot posts"""
    url = "https://api.reddit.com/r/{}/hot/.json".format(subreddit)
    head = {"User-Agent": "Client"}
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=head, params=params)
    if response.status_code != 200:
        print("None")
        return
    results = response.json().get("data")
    for c in results.get("children"):
        print(c.get("data").get("title"))
