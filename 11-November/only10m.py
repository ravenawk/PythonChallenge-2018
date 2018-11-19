#!/usr/bin/env python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
"""Pull a cisco list of 10Meg devices."""

from netmiko import ConnectHandler
import getpass
import argparse
import re


def Main():
    """Run if run as a program."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--device_os", type=str, default="cisco_ios",
                        help='Device OS default=Cisco IOS', metavar="")
    parser.add_argument("-n", "--hostname", required=True,
                        help='Hostname of device', metavar="")
    parser.add_argument("-u", "--user", type=str, default="admin",
                        help='user to connect with default=admin', metavar="")
    args = parser.parse_args()

    password = getpass.getpass()
    hostname = args.hostname + ".ne.pvhmc.org"
    cisco = {'device_type': args.device_os,
             'ip': hostname,
             'username': args.user,
             'password': password,
             }

    net_connect = ConnectHandler(**cisco)
    rawoutput = net_connect.send_command("show interfaces status")
    match10m = re.compile(r'-10\s')
    seperatelines = rawoutput.split("\n")
    for line in seperatelines:
        mo = match10m.search(line)
        if mo != None:
            newline = line.split()
            print(newline[0], newline[3], newline[4])

if __name__ == "__main__":
    Main()
