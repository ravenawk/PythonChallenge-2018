#!/usr/bin/env python3
"""Pull in cisco config."""

from netmiko import ConnectHandler
import getpass
import argparse


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
    print(hostname)
    cisco = {'device_type': args.device_os,
             'ip': hostname,
             'username': args.user,
             'password': password,
             }

    net_connect = ConnectHandler(**cisco)
    output = net_connect.send_command("show run")
    print(output)

    with open(args.hostname, 'w') as conf_file:
        conf_file.write(output)


if __name__ == "__main__":
    Main()

