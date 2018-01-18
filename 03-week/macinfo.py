#!/usr/bin/env python3
"""Program to get internet IP info."""

import requests
import argparse


def getmacinfo(website):
    """Get ip info from website."""
    inforequest = requests.get(website)
    infobyte = inforequest.content
    macinfo = infobyte.decode("utf-8")

    tabular = "{:<7} : {:<25}"
    print()
    print(tabular.format("Vendor", macinfo))
    print()


def Main():
    """Run if script is run."""
    website = "http://api.macvendors.com/"

    parser = argparse.ArgumentParser()
    parser.add_argument("mac_address", type=str, help='MAC address to lookup',
                        metavar="mac")
    args = parser.parse_args()

    website = website + args.mac_address
    getmacinfo(website)


if __name__ == "__main__":
    Main()
