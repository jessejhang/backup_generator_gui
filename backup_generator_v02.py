from tkinter.filedialog import askdirectory
import shutil, os, errno, sys
import datetime


def copy(src, dest):
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print('Directory not copied. Error: %s' % e)

text = askdirectory()

if text != '':
    src = text
    dest = src + '_' + datetime.datetime.today().strftime('%Y%m%d')
    copy(src, dest)






