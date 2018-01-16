#!/usr/bin/env python3
"""Program to get internet IP info."""

import json
import requests

website = "http://ip-api.com/json"


def getipinfo(website):
    "Get ip info from site"
    ipinfo = json.loads(requests.get(website))
    print(ipinfo)


def Main():
    "Run if script is run."
    getipinfo(website)


if __name__ == "__main__":
    Main()
