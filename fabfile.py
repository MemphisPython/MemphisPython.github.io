from datetime import date
from fabric.api import env, run, cd, local
from fabric.operations import put
from fabric import colors 
from fabric.contrib.files import exists

REMOTE_PROJECT_DIR = '/var/www/mempy.org'
env.hosts = ['root@mempy.org', ]

def backup():
    """ make a .tgz of existing content """
    backup_file = "%s/backup-%s.tgz" % (REMOTE_PROJECT_DIR, date.today())
    
    if exists("%s/*tgz" % REMOTE_PROJECT_DIR):
        rm_file("*tgz")

    with cd(REMOTE_PROJECT_DIR):
        cmd = "tar -czf %s *" % backup_file
        run(cmd)
        print(colors.green("Created backup: %s" % backup_file))

def list_backups():
    """ List the automatically generated backup files """
    with cd(REMOTE_PROJECT_DIR):
        run("ls -l backup-*")

def rm_file(filename):
    """ Delete the specified file """
    with cd(REMOTE_PROJECT_DIR):
        if exists(filename):
            run("rm %s" % filename)
            print(colors.yellow("Removed %s" % filename))
            
def upload():
    results = put(local_path="output/*", remote_path=REMOTE_PROJECT_DIR)

def deploy():
    """ deploy html content to remote directory """
    local("make clean && make html")
    backup() 
    upload() 
