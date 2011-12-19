from datetime import date
from fabric.api import env, run, cd 
from fabric.operations import put
from fabric.colors import green, red, yellow
from fabric.contrib.files import exists

REMOTE_PROJECT_DIR = '/kunden/homepages/25/d191953947/htdocs/sites/mempy.org'
env.hosts = ['u43760566@s191953969.onlinehome.us', ]

def backup():
    """ make a .tgz of existing content """
    backup_file = "%s/backup-%s.tgz" % (REMOTE_PROJECT_DIR, date.today())
    
    if exists("%s/*tgz" % REMOTE_PROJECT_DIR):
        result = run("rm *tgz")
        print(yellow("Removed existing backup files"))

    with cd(REMOTE_PROJECT_DIR):
        cmd = "tar -czf %s *" % backup_file
        run(cmd)
        print(green("Created backup: %s" % backup_file))

def upload():
    results = put(local_path="html/*", remote_path="~/sites/mempy.org")

def deploy():
    """ deploy html content to remote directory """
    backup() 
    upload() 
