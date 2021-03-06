#!/usr/bin/python3
"""full deploy"""
from fabric.api import *
from fabric.operations import run, put, sudo
import os.path
from datetime import datetime
from fabric.api import local


env.hosts = ['104.196.106.105', '34.75.199.74']
env.user = 'ubuntu'


def do_pack():
    """ generates a .tgz archive from the contents of the web_static folder"""
    date = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    filepath = "versions/web_static_{}.tgz".format(date)
    local("mkdir -p versions")
    local("tar -cvzf {} web_static".format(filepath))
    print(filepath)
    return filepath


def do_deploy(archive_path):
    """ Fabric script (based on the file 1-pack_web_static.py)
    that distributes an archive to your web servers,
     using the function do_deploy """
    if (os.path.exists(archive_path) is False):
        return False

    try:
        file = archive_path.split("/")[-1]
        name = file.split(".")[0]
        tmp = ("/data/web_static/releases/")

        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}{}".format(tmp, name))
        run("sudo tar -xzf /tmp/{}.tgz -C {}{}".format(name, tmp, name))
        run("sudo rm /tmp/{}".format(file))
        run("sudo cp {}{}/web_static/* {}{}/".format(tmp, name, tmp, name))
        run("sudo rm -rf {}{}/web_static".format(tmp, name))
        run('sudo rm -rf /data/web_static/current')
        run("sudo ln -s {}{} /data/web_static/current".format(tmp, name))
        return True
    except Exception:
        return False


def deploy():
    """ Task 3 """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
