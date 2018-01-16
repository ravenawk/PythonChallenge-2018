#!/usr/bin/env python3
"""Program to get internet IP info."""

import json
import requests
# from pprint import pprint

website = "http://ip-api.com/json/8.8.8.8"


def getipinfo(website):
    """Get ip info from website."""
    inforequest = requests.get(website)
    infobyte = inforequest.content
    return json.loads(infobyte)


def printinfo(ipinfo):
    """Print out the Ip info."""
    print("IP : {}".format(ipinfo['query']))
    print("ISP: {}".format(ipinfo['isp']))
    print("City: {}".format(ipinfo['city']))
    print("Country: {}".format(ipinfo['country']))
    print("Country Code: {}".format(ipinfo['countryCode']))


def Main():
    """Run if script is run."""
    ipinfo = getipinfo(website)
    printinfo(ipinfo)


if __name__ == "__main__":
    Main()
