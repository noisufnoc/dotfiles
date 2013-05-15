#!/usr/bin/env python

__author__ = 'noisufnoc'

# Link dotfiles to .dotfiles for managing with git

import os

HOMEDIR = os.path.expanduser('~')
DIR = '%s/.dotfiles' % HOMEDIR
OLDDIR = '%s/.dotfiles_old' % HOMEDIR
FILES = []

# Backup existing files in OLDDIR
#os.rename()
#os.makedirs(OLDDIR)

print HOMEDIR
print DIR
print OLDDIR

# mv files and create symlinks
#os.symlink()

# done, this script is done.


