#!/usr/bin/env python

__author__ = 'noisufnoc'

# Link dotfiles to .dotfiles for managing with git
# Similar to https://github.com/michaeljsmalley/dotfiles, but in py.

import os

HOMEDIR = os.path.expanduser('~')
DIR = '%s/.dotfiles' % HOMEDIR
OLDDIR = '%s/.dotfiles_old' % HOMEDIR
FILES = []

# Backup existing files in OLDDIR
if not os.path.exists(OLDDIR):
    os.makedirs(OLDDIR)


print HOMEDIR
print DIR
print OLDDIR

# mv files and create symlinks
if not os.path.exists(DIR):
    os.makedirs(DIR)


#os.symlink()
#os.rename()

# done, this script is done.


