#!/usr/bin/python3
# Author Stephen Kennedy
import os

user_path = os.getenv("HOME")
reset = "reset_master.py"
final_path = ("%s/%s" % (user_path, reset))

os.system("git fetch origin")
os.system("git reset --hard origin/master")
os.system("git pull")
os.system("chmod 755 master")
os.system("%s/master" % (final_path))
