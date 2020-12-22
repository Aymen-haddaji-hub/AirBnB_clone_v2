#!/usr/bin/python3
""" abric module to push files"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """ generates a .tgz archive from the contents of the web_static folder"""
    date = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    filepath = "versions/web_static_{}.tgz".format(date)
    local("mkdir -p versions")
    local("tar -cvzf {} web_static".format(filepath))
    return filepath
