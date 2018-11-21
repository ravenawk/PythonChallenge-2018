#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
"""Pull a Cisco list of 10Meg devices."""

from netmiko import ConnectHandler
import getpass
import argparse
import re


def main():
    """Run if as run as a program. Parsing"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--device_os", type=str, default="cisco_ios",
                        help='Device OS default=Cisco IOS', metavar="")
    parser.add_argument("-D", "--domain", type=str, default="ne.pvhmc.org",
                        help='Domain, default is=ne.pvhmc.org', metavar="")
    parser.add_argument("-n", "--hostname", required=True,
                        help='Hostname of device', metavar="")
    parser.add_argument("-u", "--user", type=str, default="admin",
                        help='user to connect with default=admin', metavar="")
    args = parser.parse_args()

    password = getpass.getpass()
    hostname = args.hostname + "." + args.domain
    cisco = {'device_type': args.device_os,
             'ip': hostname,
             'username': args.user,
             'password': password,
             }

    net_connect = ConnectHandler(**cisco)
    raw_output = net_connect.send_command("show interfaces status")
    match10m = re.compile(r'-10\s')
    for line in raw_output.split("\n"):
        mo = match10m.search(line)
        if mo is not None:
            newline = line.split()
            print(f"{newline[0]}, {newline[3]}, {newline[4]}")
            interface_mac = net_connect.send_command(f"show mac address-table interface {newline[0]}")
            match_mac = re.compile(r"([0-9]|[a-f]){4}[/.]([0-9]|[a-f]){4}[/.]([0-9]|[a-f]){4}")
            for i in interface_mac.split("\n"):
                mo2 = match_mac.search(i)
                if mo2 is not None:
                    print(mo2.group())


if __name__ == "__main__":
    main()
