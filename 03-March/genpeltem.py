#!/usr/bin/env python3
"""Pull in cisco config."""

import argparse
import datetime


def Main():
    """Run if run as a program."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-T", "--title", type=str, required=True,
                        help='Title for site, also generates the slug', metavar="")
    parser.add_argument("-c", "--category", required=True,
                        help='Category or categories of post', metavar="")
    parser.add_argument("-t", "--tags", type=str, required=True,
                        help="Tags for post", metavar="")
    parser.add_argument("-a", "--author", type=str, default="Pat Martin",
                        help="Author of post", metavar="")
    args = parser.parse_args()

    now = datetime.datetime.now() 
    slug = args.title.replace(" ","-").lower()

    with open("{}.md".format(slug), 'w') as f:
        f.write("Title: {}\n".format(args.title))
        f.write("Date: {}-{}-{} {}:{}\n".format(now.year,now.month,now.day,now.hour,now.minute))
        f.write("Modified: {}-{}-{} {}:{}\n".format(now.year,now.month,now.day,now.hour,now.minute))
        f.write("Category: {}\n".format(args.category))
        f.write("Slug: {}\n".format(slug))
        f.write("Authors: {}\n".format(args.author))
        f.write("Summary: \n")

if __name__ == "__main__":
    Main()