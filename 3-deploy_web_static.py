#!/usr/bin/python3
'''
Fabric script that distributes an archive to web servers
using deploy
'''

import os
from datetime import datetime
from fabric.api import env, local, put, run, runs_once


env.hosts = ['107.23.91.47', '35.174.211.188']


@runs_once
def do_pack():
    """Static files archives"""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    time = datetime.now()
    res = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        time.year,
        time.month,
        time.day,
