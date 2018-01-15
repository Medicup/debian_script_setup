#!/usr/bin/python3
# Author Stephen Kennedy
import os

user_path = os.getenv("HOME")
final_path = ("%s/%s" % (user_path, myPython))

os.system("git fetch origin")
os.system("git reset --hard origin/master")
os.system("git pull")
os.system("chmod 755 master")
os.system("%s/master" (final_path))
