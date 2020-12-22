#!usr/bin/python3
""" fabric module to push files"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    time_str = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    pa = "versions/web_static_{}.tgz".format(time_str)
    local("mkdir -p versions")
    local("tar -cvzf {} web_static".format(pa))
    return pa
