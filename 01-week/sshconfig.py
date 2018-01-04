#!/usr/bin/env python3
"""Program to add hosts to ssh config file and create aliases."""

import argparse

def sshconfig_entry(host, diffieh):
    """Print a line of the .ssh config."""
    print("Host {}".format(host))
    print("  Hostname {}".format(host))
    print("  Port {}".format(22))
    print("  User {}".format("admin"))
    if diffieh:
        print("  KexAlgorithms +diffie-hellman-group1-sha1")

    alias_entry(host)

def alias_entry(host):
    """Print a line in .alias file."""
    print('alias {0}="ssh s-{0}"'.format(host))


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--type", dest='contype', action='store',
                        choices=['s','t'],
                        help='s for ssh, t for telnet')
    parser.add_argument("-n", "--hostname", help='Hostname of device')
    args = parser.parse_args()
    

if __name__ == "__main__":
    Main()
