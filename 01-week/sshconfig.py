#!/usr/bin/env python3
"""Program to add hosts to ssh config file and create aliases."""

import argparse


def sshconfig_entry(host, domain, user, diffieh):
    """Print a line of the .ssh config."""
    print("Host {}".format(host))
    print("  Hostname {}.{}".format(host, domain))
    print("  Port {}".format(22))
    print("  User {}".format(user))
    if diffieh:
        print("  KexAlgorithms +diffie-hellman-group1-sha1")
    alias_entry(host)


def alias_entry(host):
    """Print a line in .alias file."""
    print('alias s-{0}="ssh {0}"'.format(host))


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--type", choices=['s', 't'], default='s',
                        help='s for ssh, t for telnet', metavar="")
    parser.add_argument("-u", "--user", type=str, default="admin",
                        help='user to connect with default=admin', metavar="")
    parser.add_argument("-d", "--domain", type=str, default="ne.pvhmc.org",
                        help='Domain name default=ne.pvhmc.org', metavar="")
    parser.add_argument("-D", "--diffie", action='store_true',
                        help='Set diffie-hellman flag (used in old ssh)')
    parser.add_argument("-n", "--hostname", required=True,
                        help='Hostname of device', metavar="")
    args = parser.parse_args()
    if args.type == 's':
        sshconfig_entry(args.hostname, args.domain, args.user, args.diffie)
    elif args.type == 't':
        print(args)



if __name__ == "__main__":
    Main()
