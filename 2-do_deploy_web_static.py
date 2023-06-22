#!/usr/bin/python3
"""deploy web static"""
from fabric import task
from fabric.api import env, put, run

@task
def do_deploy(archive_path):
    """Deploys an archive to the web servers."""

    if not exists(archive_path):
        return False

    put(archive_path, '/tmp/')
    run('tar -xzf /tmp/{} -C /data/web_static/releases/'.format(archive_path.split('/')[-1]))
    run('rm /tmp/{}'.format(archive_path))
    run('rm -rf /data/web_static/current')
    run('ln -s /data/web_static/releases/{} /data/web_static/current'.format(archive_path.split('/')[-1]))

    return True

if __name__ == '__main__':
    env.hosts = ['3.83.244.201', '54.196.238.81']
    env.user = 'username'
    env.key_file = 'path/to/key_file'

    if do_deploy('archive.tgz'):
        print('Deployment successful!')
    else:
        print('Deployment failed!')
