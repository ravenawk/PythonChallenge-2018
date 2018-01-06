#!/usr/bin/env python3
"""Program to add hosts to ssh config file and create aliases."""

import argparse
import os


def sshconf(host, domain, user, diffieh, configfile):
    """Print an entry for .ssh config."""
    with open(configfile, 'a') as sshconf:
        sshconf.write("Host {}\n".format(host))
        sshconf.write("  Hostname {}.{}\n".format(host, domain))
        sshconf.write("  Port {}\n".format(22))
        sshconf.write("  User {}\n".format(user))
        if diffieh:
            sshconf.write("  KexAlgorithms +diffie-hellman-group1-sha1\n")
        sshconf.write("\n")
    return


def alias_entry(host, domain, contype, aliasfile):
    """Print a line in .c-aliases file."""
    with open(aliasfile, 'a') as aliases:
        if contype == 's':
            aliases.write('alias {0}="ssh {0}"\n'.format(host))
        elif contype == 't':
            aliases.write('alias {0}="telnet {0}.{1}"\n'.format(host, domain))
    return


def entry_check(host, filename):
    """Check if host is in a file."""
    if not os.path.isfile(filename):
        return False
    with open(filename) as lines:
        for line in lines:
            if host in line:
                return True
    return False


def Main():
    """Run if run as a program."""
    aliasfile = os.path.expanduser("~/.c-aliases")
    sshconfig = os.path.expanduser("~/.ssh/config")

    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--remove", action='store_true',
                        help="Remove entry")
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

    if entry_check(args.hostname, sshconfig):
        if args.remove:
            print("removing ssh")
    elif args.type == 's':
        sshconf(args.hostname, args.domain, args.user, args.diffie, sshconfig)

    if entry_check(args.hostname, aliasfile):
        if args.remove:
            print("removing alias")
    else:
        alias_entry(args.hostname, args.domain, args.type, aliasfile)
    return


if __name__ == "__main__":
    Main()
