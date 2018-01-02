#!/usr/bin/env python3
"""Program to add hosts to ssh config file and create aliases."""


def sshconfig_entry(host, dh):
    """Print a line of the .ssh config."""
    print("Host {}".format(host))
    print("  Hostname {}".format(host))
    print("  Port {}".format(22))
    print("  User {}".format("admin"))
    if dh:
        print("  KexAlgorithms +diffie-hellman-group1-sha1")

    alias_entry(host)

def alias_entry(host):
    """Print a line in .alias """
    print('alias {0}="ssh s-{0}"'.format(host))


if __name__ == "__main__":
    somehost = "somehost"
    dh = True
    sshconfig_entry(somehost, dh)
