#!/usr/bin/env python

__author__ = 'noisufnoc'

# Link dotfiles to .dotfiles for managing with git
# Similar to https://github.com/michaeljsmalley/dotfiles, but in py.

import os

HOMEDIR = os.path.expanduser('~')
DIR = '%s/.dotfiles' % HOMEDIR
OLDDIR = '%s/.dotfiles_old' % HOMEDIR
FILES = ['foo', 'bar']

# Backup existing files in OLDDIR
if not os.path.exists(OLDDIR):
    os.makedirs(OLDDIR)

# mv files and create symlinks
if not os.path.exists(DIR):
    os.makedirs(DIR)

for file in FILES:
    file_orig = '%s/.%s' % (HOMEDIR, file)
    file_back = '%s/%s' % (OLDDIR, file)
    file_link = '%s/%s' % (DIR, file)

    print 'symlink %s to %s' % (file_link, file_orig)

    if not os.path.exists(file_back):
        print 'I\'m moving %s' % file_orig
        print 'New Path: %s' % file_back
        os.rename(file_orig, file_back)

    try:
        os.symlink(file_link, file_orig)
    except:
        print '%s exists! moving on' % file_link

# done, this script is done.


