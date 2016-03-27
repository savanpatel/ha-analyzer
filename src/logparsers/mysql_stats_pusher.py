#!/usr/bin/python

#------------------------------------------------------------------------------#
#  reads tsv file for haproxy stats info and pushes to mysql                   #
#                                                                              #
#                                                                              #
#                                                                              #
#Read more for mysql connector at:                                             #
#https://dev.mysql.com/doc/connector-python/en/connector-python-obtaining.html #
#                                                                              #
#                                                                              #
#  @author: Savan Patel                                                        #
#           savanpatel3@gmail.com                                              #
#------------------------------------------------------------------------------#

import ConfigFileParser
import logging
import mysql.connector
import time
import sys
import os

#colors for printing
CSI="\x1B["
reset=CSI+"m"
redColor = '\033[91m'
blueColor = '\033[94m'
#initialize config file.
if len(sys.argv) < 2:
 print "\n\n"
 print "=========================================================================================="
 print  redColor + "No config file provided."
 print  redColor + "Command : " + reset + blueColor  + "./mysql-stats-pusher <configFile>" + reset
 print "=========================================================================================="
 print "\n\n"
 exit(-1)

configFilePath = sys.argv[1]

#converts tsv line to dictionary hash
def getStatsData(tsvLine):
    tsvLine = tsvLine[:-1]
    tsvLineSplit = tsvLine.split("\t")
    statsData = {}
    statsData["date"] = tsvLineSplit[0]
    statsData["processnamepid"] = tsvLineSplit[1]
    statsData["clientip"] = tsvLineSplit[2]
    statsData["clientport"] = tsvLineSplit[3]
    statsData["accept_date"] = tsvLineSplit[4]
    statsData["frontend_listener"] = tsvLineSplit[5]
    statsData["backend_name"] = tsvLineSplit[6]
    statsData["server_name"] = tsvLineSplit[7]
    statsData["Tq"] = tsvLineSplit[8]
    statsData["Tw"] = tsvLineSplit[9]
    statsData["Tc"] = tsvLineSplit[10]
    statsData["Tr"] = tsvLineSplit[11]
    statsData["Tt"] = tsvLineSplit[12]
    statsData["status_code"] = tsvLineSplit[13]
    statsData["ac"] = tsvLineSplit[14]
    statsData["fc"] = tsvLineSplit[15]
    statsData["bc"] = tsvLineSplit[16]
    statsData["sc"] = tsvLineSplit[17]
    statsData["rc"] = tsvLineSplit[18]
    statsData["srv_queue"] = tsvLineSplit[19]
    statsData["backend_queue"] = tsvLineSplit[20]
    statsData["http_request"] = tsvLineSplit[21]

    return statsData


try:
   CONFIG = ConfigFileParser.parse(configFilePath)
except Exception as e:
   print str(e)
   exit(-1)

if "syncinterval" not in CONFIG:
    CONFIG["syncinterval"] = 0

if "log" not in CONFIG:
    CONFIG["log"] = "/tmp/ha-analyzer.log"

if "tsvfile" not in CONFIG:
    CONFIG["tsvfile"] = "/tmp/tsvfile.tsv"

if not os.path.isfile(CONFIG["tsvfile"]):
   open(CONFIG["tsvfile"], 'a').close()

logging.basicConfig(filename=CONFIG["log"],level=logging.DEBUG,
                    format='%(asctime)s.%(msecs)d %(levelname)s %(module)s - %(funcName)s: %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S")
logging.info("Log initialized.")

try:
   cnx = mysql.connector.connect(user=CONFIG["mysqluser"], database=CONFIG["mysqldatabase"], host=CONFIG["mysqlhost"], port=CONFIG["mysqlport"], password=CONFIG["mysqlpassword"])
   insert_stats = ("INSERT INTO ha_stats "
                   " (date, processnamepid, clientip, clientport, accept_date, frontend_listener, backend_name, server_name, Tq, Tw, Tc, Tr, Tt, status_code, ac, fc, bc, sc, rc, srv_queue, backend_queue, http_request) "
                   "VALUES (%(date)s, %(processnamepid)s, %(clientip)s, %(clientport)s, %(accept_date)s, %(frontend_listener)s, %(backend_name)s, %(server_name)s, %(Tq)s, %(Tw)s, %(Tc)s, %(Tr)s, %(Tt)s, %(status_code)s, %(ac)s, %(fc)s, %(bc)s, %(sc)s, %(rc)s, %(srv_queue)s, %(backend_queue)s, %(http_request)s)")
   cursor = cnx.cursor()

   tsvStatsFile = open(CONFIG["tsvfile"], 'r')
   tsvStatsFile.seek(0,2)

   while True:
       line = ''
       time.sleep(float(CONFIG["syncinterval"]))
       while len(line) == 0 or line[-1] != '\n':
           tail = tsvStatsFile.readline()
           if tail == '':
               time.sleep(0.1)
               continue
           line += tail
           statsData = getStatsData(line)
           try:
              cursor.execute(insert_stats, statsData)
              cnx.commit()
           except Exception as e:
              logging.error("statsData " + str(statsData))
              logging.error(str(e))

except mysql.connector.Error as err:
    logging.error(str(err))
else:
  cnx.close()
  exit(-1)
