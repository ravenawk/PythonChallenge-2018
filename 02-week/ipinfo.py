#!/usr/bin/env python3
"""Program to get internet IP info."""

import json
import requests

website = "http://ip-api.com"


def getipinfo(website):
    ipinfo = requests.get(website)
    print(ipinfo)


def Main():
    getipinfo(website)
