import sys, shutil, os, errno, datetime
def copy(src, dest):
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print('Directory not copied. Error: %s' % e)

src = 'D://NIP_DB_PLUS'
dest = src + '_' + datetime.datetime.today().strftime('%Y%m%d')
copy(src, dest)

