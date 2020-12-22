#!/usr/bin/python3
""" Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
 using the function do_deploy """
from fabric.api import *
from fabric.operations import run, put, sudo
import os.path
env.hosts = ['104.196.106.105', '34.75.199.74']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """ Fabric script (based on the file 1-pack_web_static.py)
    that distributes an archive to your web servers,
     using the function do_deploy """
    if (os.path.exists(archive_path) is False):
        return False

    try:
        file = archive_path.split("/")[-1]
        tmp = ("/data/web_static/releases/" + file.split(".")[0])

        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(tmp))
        run("sudo tar -xzf /tmp/{} -C {}".format(file, tmp))
        run("sudo rm /tmp/{}".format(file))
        run("sudo mv {}/web_static/* {}/".format(tmp, tmp))
        run("sudo rm -rf {}/web_static".format(tmp))
        run('sudo rm -rf /data/web_static/current')
        run("sudo ln -s {} /data/web_static/current".format(tmp))
        return True
    except Exception:
        return False
