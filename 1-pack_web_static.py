#!usr/bin/python3
""" fabric module to push files"""
import os
from fabric.api import local
from datetime import datetime


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    time_str = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    path_str = "versions/web_static_{}.tgz".format(time_str)
    var = "tar -cvzf {} web_static".format(path_str)
    local("mkdir -p versions")
    local(var)
    if os.path.exists(path_str):
        return path_str
    else:
        return None
