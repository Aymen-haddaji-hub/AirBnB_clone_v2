#!/usr/bin/python3
""" Task 1 """
from datetime import datetime
from fabric.api import local


def do_pack():
    """ Task 1 """
    date = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    filepath = "versions/web_static_{}.tgz".format(date)
    local("mkdir -p versions")
    local("tar -cvzf {} web_static".format(filepath))
    return filepath
