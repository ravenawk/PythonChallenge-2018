#!/usr/bin/env python3
"""Program to add hosts to ssh config file and create aliases."""

import argparse
import os


def sshconf(host, domain, user, diffieh):
    """Print a line of the .ssh config."""
    if os.path.isfile(os.path.expanduser("~/.ssh/config")):
        with open(os.path.expanduser("~/.ssh/config"), 'r') as sshconf:
            for line in sshconf:
                if line == "Host {}\n".format(host):
                    print("Connection already exists")
                    return

    with open(os.path.expanduser("~/.ssh/config"), 'a') as sshconf:
        sshconf.write("Host {}\n".format(host))
        sshconf.write("  Hostname {}.{}\n".format(host, domain))
        sshconf.write("  Port {}\n".format(22))
        sshconf.write("  User {}\n".format(user))
        if diffieh:
            sshconf.write("  KexAlgorithms +diffie-hellman-group1-sha1\n")
        sshconf.write("\n")

        alias_entry(host, 's')


def alias_entry(host, contype):
    """Print a line in .alias file."""
    aliasfile = os.path.expanduser("~/.c-aliases")
    with open(aliasfile, 'a') as aliases:
        if contype == 's':
            aliases.write('alias s-{0}="ssh {0}"\n'.format(host))


def Main():
    """Run if run as a program."""
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
        sshconf(args.hostname, args.domain, args.user, args.diffie)
    elif args.type == 't':
        print(args)


if __name__ == "__main__":
    Main()
