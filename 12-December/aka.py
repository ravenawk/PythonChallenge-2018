#!/usr/bin/env python
"""Manage unix style aliases"""
import argparse


def add_alias(alias_to_add):
    """Add an alias to the alias file"""
    print(f"Add to {alias_to_add} file")
    pass


def remove_alias():
    pass


def print_aliases():
    pass


def main():
    """Argument parsing"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--add", help="Add an item to the alias file")
    args = parser.parse_args()

    if args.add:
        add_alias(args.add)


if __name__ == "__main__":
    main()
