"""Tool for creating RouterOS configuration backup

It can be used as an interactive tool from CLI or for unattended backups in 
containers, in which case, it is using following environment variables:

ROS_HOST: for storing Ip address or hostname (e.g., 192.168.1.1)
ROS_USER: username for making backups
ROS_PASS: password for provided username

When used in CLI, it will prompt for password if -p (--password) flag
not provided. Config will be printed to the stdout if -f (--file) omitted. 
"""


from rosbackup.rosdevice import ROSDevice


__version__ = '1.1.0'
__all__ = ('ROSDevice')