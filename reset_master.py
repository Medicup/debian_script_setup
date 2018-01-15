#!/usr/bin/python3
# Author Stephen Kennedy
import os

os.system("git fetch origin")
os.system("git reset --hard origin/master")
os.system("git pull")
os.system("chmod 755 master")
