#!/usr/bin/python

#------------------------------------------------------------------------------#
#  reads the haproxy log file, filters out lines                               #
#  and pushes to haproxy-log-analyzer.                                         #
#                                                                              #
#  syncs log at the interval of the time provided                              #
#  in config file.                                                             #
#                                                                              #
#  @author: Savan Patel                                                        #
#           savanpatel3@gmail.com                                              #
#------------------------------------------------------------------------------#

import ConfigFileParser
import HaproxyFilterRegex
import HaproxyLogParser
import TSVFileUtils
import time
import logging
import sys
import os.path

CSI="\x1B["
reset=CSI+"m"
redColor = '\033[91m'
blueColor = '\033[94m'
#initialize config file.
if len(sys.argv) < 2:
 print "\n\n"
 print "=========================================================================================="
 print  redColor + "No config file provided."
 print  redColor + "Command : " + reset + blueColor  + "./haproxy-log-puller <configFile>" + reset
 print "=========================================================================================="
 print "\n\n"
 exit(-1)

configFilePath = sys.argv[1]

try:
   CONFIG = ConfigFileParser.parse(configFilePath)
except Exception as e:
   print str(e)
   exit(-1)


#initialize log file
if "log" not in CONFIG:
    CONFIG["log"] = "/tmp/ha-analyzer.log"

if "tsvfile" not in CONFIG:
    CONFIG["tsvfile"] = "/tmp/tsvfile.tsv"

logging.basicConfig(filename=CONFIG["log"],level=logging.DEBUG,
                    format='%(asctime)s.%(msecs)d %(levelname)s %(module)s - %(funcName)s: %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S")
logging.info("Log initialized.")


#pull log lines and push to haproxy-log-analyzer
if "log" not in CONFIG:
    CONFIG["haproxylog"] = "/var/logs/haproxy.log"

if "syncinterval" not in CONFIG:
    CONFIG["syncinterval"] = 0

if not os.path.isfile(CONFIG["haproxylog"]):
    logging.error("No haproxy log file found at " + CONFIG["haproxylog"])
    exit(-1)

haproxyLogFile = open(CONFIG["haproxylog"], 'r')

#seek to the end of file
haproxyLogFile.seek(0,2)
#get regular expression for log matching
rg = HaproxyFilterRegex.getHaproxyFilterRegex()


while True:
    line = ''
    time.sleep(float(CONFIG["syncinterval"]))
    while len(line) == 0 or line[-1] != '\n':
        tail = haproxyLogFile.readline()
        if tail == '':
            time.sleep(0.1)
            continue
        line += tail
        check = rg.search(line)
        if check:
            try:
                HAPROXYLOG = HaproxyLogParser.toHaproxyStats(line)
                if HAPROXYLOG:
                   try:
                       TSVFileUtils.pushToTSVFile(HAPROXYLOG, CONFIG["tsvfile"])
                   except Exception as e:
                       logging.error(str(e))
                       print str(e)
                       logging.error("Exiting.")
                       exit(-1)
            except Exception as e:
                logging.error(str(e))
