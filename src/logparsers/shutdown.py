#!/usr/bin/python

#------------------------------------------------------------------------------#
#  shuts down ha-analyzer                                                      #
#  and pushes to haproxy-log-analyzer.                                         #
#                                                                              #
#                                                                              #
#  @author: Savan Patel                                                        #
#           savanpatel3@gmail.com                                              #
#------------------------------------------------------------------------------#


import sys
import subprocess
import os
import signal

CSI="\x1B["
reset=CSI+"m"
redColor = '\033[91m'
blueColor = '\033[94m'

pullerpidfilename = "/tmp/ha-analyzer.puller.pid"
mysqlprocessorpidfilename = "/tmp/ha-analyzer.mysql-pusher.pid"


#get pid from pid file
def getPid(fileName):
   with open(fileName,"r") as file:
      pid = file.readline()
      file.close()
      return pid

#shutdown puller process
if os.path.isfile(pullerpidfilename):
   pullerpid = getPid(pullerpidfilename)
   os.kill(int(pullerpid), signal.SIGTERM)
   print "Shutdown haproxy puller [ pid ] " + pullerpid

#shutdown pusher process
if os.path.isfile(mysqlprocessorpidfilename):
   mysqlpusherpid = getPid(mysqlprocessorpidfilename)
   os.kill(int(mysqlpusherpid), signal.SIGTERM)
   print "Shutdown mysql stats pusher [ pid ] " + mysqlpusherpid

print "Shutdown successful."
