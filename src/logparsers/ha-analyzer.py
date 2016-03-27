#!/usr/bin/python

#------------------------------------------------------------------------------#
#  runner class for log processors.                                            #
#  runs : 1) haproxy-log-puller                                                #
#         2) mysql_stats_pusher                                                #
#                                                                              #
#                                                                              #
#  checks for the existing pid for haproxy-log-puller and mysql_stats_pusher   #
#  exits if process is already running.                                        #
#  Command : ./ha-analyzer <configFile>                                        #
#                                                                              #
#                                                                              #
#  @author: Savan Patel                                                        #
#           savanpatel3@gmail.com                                              #
#------------------------------------------------------------------------------#

import ConfigFileParser
import sys
import subprocess
import os

CSI="\x1B["
reset=CSI+"m"
redColor = '\033[91m'
blueColor = '\033[94m'

pullerpidfilename = "/tmp/ha-analyzer.puller.pid"
mysqlprocessorpidfilename = "/tmp/ha-analyzer.mysql-pusher.pid"

#initialize config file.
if len(sys.argv) < 2:
 print "\n\n"
 print "=========================================================================================="
 print  redColor + "No config file provided." + reset
 print  redColor + "Command : " + reset + blueColor  + "./haproxy-log-puller <configFile>" + reset
 print "=========================================================================================="
 print "\n\n"
 exit(-1)

#check if pid exists
def pid_exists(pid):
   return os.path.isdir("/proc/"+str(pid))

configFilePath = sys.argv[1]
try:
   CONFIG = ConfigFileParser.parse(configFilePath)
except Exception as e:
   print str(e)
   exit(-1)

if not os.path.isfile(configFilePath):
   print  redColor + "Config file " + blueColor + "[" + configFilePath + "]" + blueColor + redColor +  " does not exists." + reset
   exit(-1)

#check if haproxy-log puller process is already running.
if os.path.isfile(pullerpidfilename):
    with open(pullerpidfilename,"r") as file:
        pullerpid = file.readline()
        if pid_exists(pullerpid):
            print redColor + "Puller Process already running with pid " + pullerpid + reset
            print redColor  + "Try killing it first." +reset
            exit(-1)

#check if mysql-stats-pusher process is already running.
if os.path.isfile(mysqlprocessorpidfilename):
    with open(mysqlprocessorpidfilename,"r") as file:
        mysqlpid = file.readline()
        if pid_exists(mysqlpid):
            print redColor + "Mysql pusher Process already running with pid " + mysqlpid + reset
            print redColor  + "Try killing it first." +reset
            exit(-1)

#start haproxy-log-puller and store its pid
print blueColor + "Starting log puller" + reset
pullerProcess = subprocess.Popen(['./haproxy-log-puller.py', configFilePath])
print blueColor + "Log puller started successfully" + reset
print redColor + "Log Puller pid : " + str(pullerProcess.pid) + reset


with open(pullerpidfilename, 'w') as pullerpidfile:
    pullerpidfile.write(str(pullerProcess.pid))
    pullerpidfile.close()
#start mysql-stats-pusher and store its pid
print blueColor + "Starting mysql stats pusher" + reset
mysqlStatsPusherProcess = subprocess.Popen(['./mysql_stats_pusher.py', configFilePath])
print blueColor + "Mysql Stats Pusher successfully" + reset
print redColor + "Mysql Stats Pusher pid : " + str(mysqlStatsPusherProcess.pid) + reset


with open(mysqlprocessorpidfilename, 'w') as  mysqlpidfile:
    mysqlpidfile.write(str(mysqlStatsPusherProcess.pid))
    mysqlpidfile.close()

print blueColor
print "============================================================== "
print "         _______                                               "
print "         |      |                                              "
print "         |     /     ______     _____          _____  _____    "
print "         |    |     |      |   |       |  /   |         |      "
print "         |     \    |      |   |       | |    |===      |      "
print "         |      \   |______|   |_____  |  \   |_____    |      "

print "                                                               "
print "         |                                                     "
print "         |                                                     "
print "         |          _____      _____     _____                 "
print "         |         |     |    |     |   |                      "
print "         |         |     |    | ___ /   | ____                 "
print "         |         | === |    |     \         |                "
print "         | ______  |     |    |_____|    _____|                "
print "                                                               "
print "=============================================================="

print reset
print "=============================================================="
print  " INITIALIZED SUCCESSFULLY"
print "=============================================================="

print redColor + "Dont forget to add logrotator for the files  : " + reset
print blueColor + " 1)" + CONFIG["tsvfile"] + reset
print blueColor + " 2)" + CONFIG["log"] + reset
print redColor + "Run shutdown.py to shutdown." + reset
