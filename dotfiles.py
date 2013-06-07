#!/usr/bin/env python

__author__ = 'noisufnoc'

# Link dotfiles to .dotfiles for managing with git
# Similar to https://github.com/michaeljsmalley/dotfiles, but in py.

# TODO: zsh installer
# TODO: clone oh-my-zsh repo

import os
import sys
import platform

if sys.version_info < (2, 6):
    print "I require 2.6 or higher"
    sys.exit(1)

HOMEDIR = os.path.expanduser('~')
DIR = '%s/.dotfiles' % HOMEDIR
OLDDIR = '%s/.dotfiles_old' % HOMEDIR
FILES = [
    'bashrc',
    'fonts',
    'inputrc',
    'screenrc',
    'ttytterrc',
    'ttytterkey',
    'vim',
    'vimrc',
    'zshrc'
]


# Backup existing files in OLDDIR
if not os.path.exists(OLDDIR):
    os.makedirs(OLDDIR)

# mv files and create symlinks
if not os.path.exists(DIR):
    os.makedirs(DIR)

for file in FILES:
    # Iterate through file list
    file_orig = '%s/.%s' % (HOMEDIR, file)
    file_back = '%s/%s' % (OLDDIR, file)
    file_link = '%s/%s' % (DIR, file)

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

if os.path.exists('%s/vim/bundle' % DIR):
    os.system('git clone https://github.com/gmarik/vundle.git %s/vim/bundle/vundle' % DIR)
    os.system('vim +BundleInstall +qall')

# I really like zsh and oh-my-zsh

if not os.path.exists('/bin/zsh') or os.path.exists('/usr/bin/zsh'):
    if platform.linux_distribution()[0] == 'Ubuntu':
        os.system('sudo apt-get install -y zsh')
    elif platform.linux_distribution()[0] == 'CentOS':
        os.system('sudo yum install -y zsh')
    else:
        print 'I don\'t know what distro you\'re running, install zsh manually!'

os.system('git clone https://github.com/robbyrussell/oh-my-zsh.git %s/.oh-my-zsh' % HOMEDIR)

# done, this script is done.
