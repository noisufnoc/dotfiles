#!/usr/bin/env python2

import os
import sys
from platform import system, system_alias, release, version, linux_distribution

__author__ = 'noisufnoc'

# Link dotfiles to .dotfiles for managing with git

# TODO improve zsh installer
# TODO probably should obey pep8
# TODO logging
# TODO test mode
# TODO move to python3
# TODO set zsh to default shell
# TODO install things like tmux
# TODO ensure zsh plugins work on new system

if sys.version_info < (2, 6):
    print "I require 2.6 or higher"
    sys.exit(1)

# Determine OS type so I can use specific dotfiles
#     think about how to set this variable

_os, release, version = system_alias(system(), release(), version())
if _os.lower() == 'linux':
    myos = 'linux'
elif _os.lower() == 'darwin':
    myos = 'osx'
elif _os.lower() == 'win32':
    myos = 'windows'
else:
    # i dunno you should check this first
    print "I'm not sure what OS you're running, lets quit."
    sys.exit(1)

HOMEDIR = os.path.expanduser('~')
DIR = '%s/.dotfiles' % HOMEDIR
OLDDIR = '%s/.dotfiles_old' % HOMEDIR
SECRETS = 'https://noisufnoc@bitbucket.org/noisufnoc/secrets.git'

# here you should build the list of secret files from priv git repo
if not os.path.exists('secret'):
    os.system('git clone %s secret' % SECRETS)

# I need to get the files in the folders and build the FILES list

cp_files = ['crossplatform/{0}'.format(i) for i in os.listdir('%s/crossplatform' % DIR)]
secret_files = ['secret/{0}'.format(i) for i in os.listdir('%s/secret' % DIR)]
os_files = [('%s/{0}' % myos).format(i) for i in os.listdir('%s/%s' % (DIR, myos))]

FILES = cp_files + secret_files + os_files

for file in FILES:
    print '%s/.%s linked to %s/%s' % (HOMEDIR, file.split('/')[1], DIR, file)

# Backup existing files in OLDDIR
if not os.path.exists(OLDDIR):
    os.makedirs(OLDDIR)

# mv files and create symlinks
if not os.path.exists(DIR):
    os.makedirs(DIR)

for file in FILES:
    # Iterate through file list
    file_orig = '%s/.%s' % (HOMEDIR, file.split('/')[1])
    file_back = '%s/%s' % (OLDDIR, file.split('/')[1])
    file_link = '%s/%s' % (DIR, file)

    # This should never fire
    if not os.path.exists(file_link):
        print 'You listed file \'%s\' that doesn\'t exist in %s, Skipping...' % (file, DIR)
        continue

    if os.path.exists(file_orig) and not os.path.islink(file_orig):
        # If the target exists and isn't a link, then back up the real file and do work.
        print 'I\'m moving %s to %s' % (file_orig, file_back)
        os.rename(file_orig, file_back)
        print 'I\'m symlinking %s to %s' % (file_link, file_orig)
        os.symlink(file_link, file_orig)
    elif not os.path.exists(file_orig):
        # File doesn't exist, but I want a symlink anyway
        print 'I\'m symlinking %s to %s' % (file_link, file_orig)
        os.symlink(file_link, file_orig)
    else:
        print 'Symlink %s exists! Moving on...' % file_link

# I use vundle, you should too.

if os.path.exists('%s/.vim/bundle' % HOMEDIR):
    os.system('git clone https://github.com/gmarik/vundle.git %s/.vim/bundle/vundle' % HOMEDIR)
    os.system('vim +PluginInstall +qall')

# I really like zsh and oh-my-zsh

if not os.path.exists('/bin/zsh') or os.path.exists('/usr/bin/zsh'):
    if linux_distribution()[0] == 'Ubuntu':
        os.system('sudo apt-get install -y zsh')
    elif linux_distribution()[0] == 'CentOS':
        os.system('sudo yum install -y zsh')
    else:
        print 'I don\'t know what distro you\'re running, install zsh manually!'

os.system('git clone https://github.com/robbyrussell/oh-my-zsh.git %s/.oh-my-zsh' % HOMEDIR)

# done, this script is done.
