#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This tool change your mac until you restart your pc or get it back in other way

#author peleon02 aka kpg_02
#date 2018-09-13
#version 1.1
#Tested in python 3.x

LICENSE:
This software is distributed under the GNU General Public License version 3
LEGAL NOTICE:
THIS SOFTWARE IS PROVIDED FOR EDUCATIONAL USE ONLY!
IF YOU ENGAGE IN ANY ILLEGAL ACTIVITY
THE AUTHOR DOES NOT TAKE ANY RESPONSIBILITY FOR IT.
BY USING THIS SOFTWARE YOU AGREE WITH THESE TERMS.
"""
import sys
import platform
import subprocess
import argparse
import re
from random import choice, randint

if (sys.version_info > (3, 0)):
    pass
else:
    print("This program was written for python 3")
    exit()


def get_arguments():
    """Create the parser to catch the arguments that are passed when calling
the program from the cli, and add their help to be shown when -h or --help
is used as argument"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mac',
                        help='Introduce your new MAC',
                        action="store")
    parser.add_argument('-i', '--interface',
                        help='The interface that the MAC will be changed',
                        action="store")
    parser.add_argument('-a', '--about',
                        help='Display iformation about me (the developer)',
                        action="store_true")
    parser.add_argument('-r', '--random',
                        help='Create a random MAC,' +
                             'to use this argument you mustn´t use -m',
                        action="store_true")
    return parser.parse_args()


args = get_arguments()


def mac_random():
    """Generate a random MAC address taking the first 3 pairs from
Cisco and Dell defined hardware, and generate the 3 last pairs randomly"""
    cisco = ["00", "40", "96"]
    dell = ["00", "14", "22"]
    mac_address = choice([cisco, dell])
    for i in range(3):
        one = choice(str(randint(0, 9)))
        two = choice(str(randint(0, 9)))
        three = (str(one + two))
        mac_address.append(three)
    return ":".join(mac_address)


def change_mac(interface, new_mac):
    """Use Linux commands to change the mac"""
    subprocess.call(["ifconfig " + str(interface) + " down"], shell=True)
    subprocess.call(["ifconfig " + str(interface) +
                     " hw ether " + str(new_mac) + " "], shell=True)
    subprocess.call(["ifconfig " + str(interface) + " up"], shell=True)


def CurrentMac():
    """Check the current MAC, taking it from the ifconfig + interface output
and taking only the MAC with Regular Expresions in this case
\w it takes any alphanumeric character"""
    output = subprocess.check_output(["ifconfig " +
                                      args.interface], shell=True)
    current_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(output))
    return current_mac


def main():
    if platform.system() != 'Linux':  # Check if isn´t running on linux
        print("This tool cannot be used if you are" +
              "not running a Linux Distribution")
        exit()
    if (args.about is True):  # Check if the -a/--about argument is passed
        print('[*] Hi, I´m peleon02 aka kpg_02,' +
              'the developer of this tool')
        print('[*] Version 1.1, it was devoloped for python 3')
        print('[*] Any suggestion for more tools' +
              'written in python are welcome')
    elif (args.random is True and args.interface is not None):
        # The above code checks if the random argument is passed and if the
        # interface is not empty
        current_mac0 = CurrentMac()
        print("[+] Your current MAC for the interface " +
              str(args.interface) + " is " + str(current_mac0.group(0)))
        random_mac = mac_random()
        change_mac(args.interface, str(random_mac))
        current_mac1 = CurrentMac()
        if current_mac0.group(0) != current_mac1.group(0):
            print("[+] Your MAC has been changed successfully")
            print("[+] Your new MAC is " + str(random_mac))
            print("[+] Your original MAC return after a reboot")
            print("[*] Script created by peleon02")
        else:
            print("[-] Something went wrong")
    elif (args.about is False and args.mac is None or
          args.interface is None):
        # The above code checks if About MAC and Interface are used,
        # and if they aren´t show the following message
        print("[-] You didn´t pass a MAC address or an Interface")
        print("[-] Make sure you use -m / --mac XX:XX:XX:XX:XX:XX for MAC")
        print("[-] You can use -r / --random instead of -m to generate a" +
              " random MAC")
        print("[-] Make sure you use -i / " +
              "--interface (Name of the interface) for the interface")
        print("[-] You can use -a/--about to know more about me")
    elif (re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",
          str(args.mac)) is None):
        print("[-] You didn´t pass a valid MAC address")
        print("[-] Remember a MAC address must have 6 pairs of " +
              "alphanumerics characters")
        exit()
    elif(args.mac is not None and args.interface is not None):
        # The above code check if the MAC argument
        # aren´t empty and the interface argument
            current_mac0 = CurrentMac()
            print("[+] Your current MAC for the interface " +
                  str(args.interface) + " is " +
                  str(current_mac0.group(0)))
            change_mac(args.interface, args.mac)
            current_mac1 = CurrentMac()
            if current_mac0.group(0) != current_mac1.group(0):
                print("[+] Your MAC has been changed successfully")
                print("[+] Your new MAC is " + current_mac1.group(0))
                print("[+] Your original MAC return after a reboot")
                print("[*] Script created by peleon02")
            else:
                print("[-] Something went wrong")
                print("[-] Make sure that you are running it as root")

    else:
        print("[-] Something went wrong")


if __name__ == '__main__':
    # Make the program only runs if is itself opening
    try:
        main()
    except Exception:
        print("[-] Something went wrong")
        print("[-] It might be a wrong interface name")
        print("[-] If ifconfig is not found try to install net-tools")
