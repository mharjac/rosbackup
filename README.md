# ROSBackup

## Summary

Simple utility for backing up RouterOS configuration.

## Installation
### Create backup user account
It is recommended to create a dedicated user account with limited permissions for backup purposes. This user should have ssh and read permissions. Please check [RouterOs manual](https://wiki.mikrotik.com/wiki/Manual:Router_AAA) if you are not sure how to do this. 

### Installation form PyPI:
```
pip3 install rosbackup
```
### Docker
You can download the image from Docker Hub:
```
docker pull mharjac/rosbackup
```
Or build it on your own:
```
docker build -t rosbackup . -f docker/Dockerfile
```
Create a volume for storing backups:
```
docker volume create mikrotik-router-1
```
Create a container:
```
docker run -d --name=mikrotik-router-1 -e ROS_HOST="https://192.168.1.1" -e ROS_USER="backusr" -e ROS_PASS="somesuperstrongpassword" --mount=src=mikrotik-router-1,dst=/backup rosbackup:latest
```
And finally, for unattended regular backups, create a cron job which will execute:
```
docker start mikrotik-router-1
```
### Install from Snap Store
```
snap install rosbackup
```
## Usage
It can be used as an interactive tool from CLI:
```
rosbackup -H https://192.168.1.1 -u user1 -p passw0rd -f ./backup.cfg
```
When used in CLI, it will prompt for password if -p (--password) flag is not provided. Also, without -f (--file) flag, config will be printed to the stdout.  

It can also be used for unattended backups (e.g., in containers), in which case, it requires following environment variables:  
* ROS_HOST: for storing IP address or hostname (e.g., 192.168.1.1)
* ROS_USER: username for making backups
* ROS_PASS: password for provided username
```
export ROS_HOST="192.168.1.1" ROS_USER="user1" ROS_PASS="passw0rd"
rosbackup
```
When executed in unattended mode, configuration backup will be saved in execution directory as `config-{time_stamp}.cfg`.
