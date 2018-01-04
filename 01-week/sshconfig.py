#!/usr/bin/env python3
"""Program to add hosts to ssh config file and create aliases."""

import argparse


def sshconfig_entry(host, user, diffieh):
    """Print a line of the .ssh config."""
    print("Host {}".format(host))
    print("  Hostname {}.ne.pvhmc.org".format(host))
    print("  Port {}".format(22))
    print("  User {}".format(user))
    if diffieh:
        print("  KexAlgorithms +diffie-hellman-group1-sha1")
    alias_entry(host)


def alias_entry(host):
    """Print a line in .alias file."""
    print('alias {0}="ssh s-{0}"'.format(host))


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--type", choices=['s', 't'],
                        help='s for ssh, t for telnet')
    parser.add_argument("-u", "--user", type=str, default="admin",
                        help='user to connect with')
    parser.add_argument("-d", "--diffie", action='store_true',
                        help='Set diffie-hellman flag (used in old ssh')
    parser.add_argument("-n", "--hostname", required=True,
                        help='Hostname of device')
    args = parser.parse_args()
    sshconfig_entry(args.hostname, args.user, args.diffie)


if __name__ == "__main__":
    Main()
