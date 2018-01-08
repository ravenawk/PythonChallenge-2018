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
                 ftprempass, ftpremdir, remfilename,):
    """Pull files with FTP."""
    os.chdir(workingdir)
    ftp = ftplib.FTP(ftpremserv)
    ftp.login(ftpremuser, ftprempass)
    ftp.cwd(ftpremdir)
    fhandle = open(remfilename, 'wb')
    ftp.retribinary('RETR' + remfilename, fhandle.write)
    ftp.close()


def pushftpfiles()
