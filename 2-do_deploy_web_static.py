#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py) \
that distributes an archive to your web servers\
using the function do_deploy """

from fabric.api import *
from os.path import exists
from datetime import datetime
from fabric.contrib.console import confirm
env.hosts = ['104.196.106.105', '34.75.232.120']
env.user = "ubuntu"
env.warn_only = True


def do_pack():
    """ generates a .tgz archive from the contents of the web_static folder"""
    date = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    filepath = "versions/web_static_{}.tgz".format(date)
    local("mkdir -p versions")
    local("tar -cvzf {} web_static".format(filepath))
    return filepath


def do_deploy(archive_path=None):
    """ Fabric script (based on the file 1-pack_web_static.py)
     that distributes an archive to your web servers,
     using the function do_deploy"""
    if exists(archive_path) is False:
        return False

    name = archive_path.split("/")[-1].split(".")[0]
    try:
        put(archive_path, "/tmp/")
        run('mkdir -p /data/web_static/releases/{}/'.format(name))
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/\
            releases/{}/'.format(name, name))
        run('rm /tmp/{}.tgz'.format(name))
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}'.format(name, name))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(name))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ \
            /data/web_static/current'.format(name))
        return True
    except Exception:
        return False
