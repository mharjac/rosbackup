"""Tool for creating RouterOS configuration backup

It can be used as an interactive tool from CLI or for unattended backups in 
containers, in which case, it is using following environment variables:

ROS_HOST: for storing Ip address or hostname (e.g., 192.168.1.1)
ROS_USER: username for making backups
ROS_PASS: password for provided username

When used in CLI, it will prompt for password if -p (--password) flag
not provided. Config will be printed to the stdout if -f (--file) omitted. 
"""


import os
import sys
import getpass
import argparse
import datetime
import rosbackup


def main():
    parser = argparse.ArgumentParser(prog="rosbackup")
    parser.add_argument("-H", "--host", help="router's IP address")
    parser.add_argument("-u", "--user", help="username for executing backup")
    parser.add_argument("-p", "--password", help="password for provided username; prompts if not provided")
    parser.add_argument("-f", "--filename", default="/dev/stdout", metavar="FILE", help="FILE to write backup; stdout if not provided")
    parser.add_argument("-v", "--version", action="store_true", help="show version")
    options = parser.parse_args()

    time_stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

    if options.version:
        print(rosbackup.__version__)
        sys.exit(0)
    elif options.host and options.user:
        username = options.user
        if options.password:
            password = options.password
        else:
            password = getpass.getpass("Input password: ")
        host = options.host
        filename = options.filename
    else:
        try:
            username = os.environ['ROS_USER']
            password = os.environ['ROS_PASS']
            host = os.environ['ROS_HOST']
            filename = f"config-{time_stamp}.cfg"
        except KeyError as err:
            sys.stderr.write(f"ERROR: Missing {err} environment variable.\n")
            sys.exit(1)

    tik = rosbackup.ROSDevice(host, username, password)
    config = tik.get_config()

    with open(filename, "w") as f:
        f.write(config)


if __name__ == "__main__":
    main()