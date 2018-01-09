#!/usr/bin/env python3
"""Program to move files via ftp and manipulate the filenames if need be."""

import paramiko
import ftplib
import os
import datetime

####################
# Assign variables #
####################


def pullftpfiles(workingdir, ftpremserv, ftpremuser,
                 ftprempass, ftpremdir, remfilename):
    """Pull files with FTP."""
    os.chdir(workingdir)
    ftp = ftplib.FTP(ftpremserv)
    ftp.login(ftpremuser, ftprempass)
    ftp.cwd(ftpremdir)
    fhandle = open(remfilename, 'wb')
    ftp.retribinary('RETR' + remfilename, fhandle.write)
    ftp.close()


def pushftpfiles(workingdir, ftpremserv, ftpremuser,
                 ftprempass, ftpremdir, remfilename):
    """Push files with FTP."""


def listdir_nohidden(path):
    for f in os.listdir(path):
        if (os.path.isfile(os.path.join(path, f))) and (not f.startswith('.')):
            yield f


def Main():
    print("test")


if __name__ == "__main__":
    Main()


   os.chdir(workingdir)

   #########################
   ### Get list of files ###
   #########################

   listoffiles = listdir_nohidden(workingdir)

   #########################
   ##  Put files with FTP ##
   #########################

   ftp = FTP(ftpserver)
   ftp.login(ftpusername,ftppassword)

    for line in listoffiles:
    putline = 'STOR ' + line + '.850'
    workfile = open(line,'rb')
    ftp.storlines(putline, workfile)
    workfile.close()
    shutil.copy(line,archivedir)
    os.chdir(archivedir)
    os.rename(line,(line+'.850'))
    os.chdir(workingdir)
    print(line)
    os.remove(line)

