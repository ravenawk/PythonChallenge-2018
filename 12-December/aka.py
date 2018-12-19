#!/usr/bin/env python3
"""Manage unix style aliases"""
import argparse
import sys


class Aka(object):

    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Manages aliases',
            usage='''git <command> [<args>]
            
            Commands:
            add     Add an alias
            delete  Delete an alias'''
        )
        parser.add_argument('command', help='Subcommand to run ')
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)


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
    Aka()
