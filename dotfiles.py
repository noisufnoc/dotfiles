#!/usr/bin/env python

__author__ = 'noisufnoc'

# Link dotfiles to .dotfiles for managing with git
# Similar to https://github.com/michaeljsmalley/dotfiles, but in py.

import os

HOMEDIR = os.path.expanduser('~')
DIR = '%s/.dotfiles' % HOMEDIR
OLDDIR = '%s/.dotfiles_old' % HOMEDIR
FILES = [
    'foo',
    'bar'
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

# done, this script is done.


