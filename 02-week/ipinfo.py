#!/usr/bin/env python3
"""Program to get internet IP info."""

import json
import requests
import argparse


def getipinfo(website):
    """Get ip info from website."""
    inforequest = requests.get(website)
    infobyte = inforequest.content

    return json.loads(infobyte)


def printinfo(ipinfo):
    """Print out the Ip info."""
    tabular = "{:<15} : {:<25}"

    print()
    print(tabular.format("IP", ipinfo['query']))
    print(tabular.format("ISP", ipinfo['isp']))
    print(tabular.format("City", ipinfo['city']))
    print(tabular.format("Country", ipinfo['country']))
    print(tabular.format("Country Code", ipinfo['countryCode']))
    print()


def Main():
    """Run if script is run."""
    website = "http://ip-api.com/json/"

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip", type=str, default="",
                        help='IP other than localhosts IP', metavar="")
    args = parser.parse_args()

    website = website + args.ip

    ipinfo = getipinfo(website)

    printinfo(ipinfo)


if __name__ == "__main__":
    Main()
