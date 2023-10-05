#!/usr/bin/python3
'''
Fabric script that distributes an archive to web servers
'''

import os
from datetime import datetime
from fabric.api import env, put, run, runs_once, local

env.hosts = ['107.23.91.47', '35.174.211.188']


def do_deploy():
    """Static files archives"""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    time = datetime.now()
    res = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        time.year,
        time.month,
        time.day,
        time.hour,
        time.minute,
        time.second
