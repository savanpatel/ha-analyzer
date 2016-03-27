
#------------------------------------------------------------------------------#
#  provides regular expression for haproxy log filtering                       #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#  @author: Savan Patel                                                        #
#           savanpatel3@gmail.com                                              #
# more about haproxy log format :                                              #                       
# https://www.haproxy.com/static/media/uploads/eng/resources/aloha_load_balancer_memo_log.pdf #
#------------------------------------------------------------------------------#

import parser
import datetime

#fetches haproxy stats from log line to dictionary.
def toHaproxyStats(haproxyLogLine):
  haproxyLogLineSplit = haproxyLogLine.split(" ")
  HAPROXYLOG = {}
  tsvOut = ''
  if len(haproxyLogLineSplit) == 20:
      dateTime = str(haproxyLogLineSplit[1]) + "-" + str(haproxyLogLineSplit[0]) + "-" + str(datetime.datetime.now().year) + "-" + str(haproxyLogLineSplit[2])
      accept_date = datetime.datetime.strptime(haproxyLogLineSplit[6][1:-5],"%d/%b/%Y:%H:%M:%S")
      requestTimeInfo = haproxyLogLineSplit[9].split("/")
      requestConcurrencyInfo = haproxyLogLineSplit[15].split("/")
      requestQueueInfo = haproxyLogLineSplit[16].split("/")

      HAPROXYLOG["date"] = str(datetime.datetime.strptime(dateTime, "%d-%b-%Y-%H:%M:%S"))
      HAPROXYLOG["processnamepid"] = haproxyLogLineSplit[4]
      HAPROXYLOG["clientip"] = haproxyLogLineSplit[5].split(":")[0]
      HAPROXYLOG["clientport"] = haproxyLogLineSplit[5].split(":")[1]
      HAPROXYLOG["accept_date"] = str(accept_date)
      HAPROXYLOG["frontend_listener"] = haproxyLogLineSplit[7]
      HAPROXYLOG["backend_name"] = haproxyLogLineSplit[8].split("/")[0]
      HAPROXYLOG["server_name"] = haproxyLogLineSplit[8].split("/")[1]
      HAPROXYLOG["Tq"] = requestTimeInfo[0]
      HAPROXYLOG["Tw"] = requestTimeInfo[1]
      HAPROXYLOG["Tc"] = requestTimeInfo[2]
      HAPROXYLOG["Tr"] = requestTimeInfo[3]
      HAPROXYLOG["Tt"] = requestTimeInfo[4]
      HAPROXYLOG["status_code"] = haproxyLogLineSplit[10]

      #actconn: total number of concurrent connections on the process when the session was logged
      #feconn: total number of concurrent connections on the frontend when the session was logged
      #beconn: total number of concurrent connections handled by the backend when the session was logged
      #srv conn: total number of concurrent connections still active on the server when the session was logged
      #retries: number of connection retries experienced by this session when trying to connect to the server

      HAPROXYLOG["ac"] = requestConcurrencyInfo[0]
      HAPROXYLOG["fc"] = requestConcurrencyInfo[1]
      HAPROXYLOG["bc"] = requestConcurrencyInfo[2]
      HAPROXYLOG["sc"] = requestConcurrencyInfo[3]
      HAPROXYLOG["rc"] = requestConcurrencyInfo[4]
      HAPROXYLOG["srv_queue"] = requestQueueInfo[0]
      HAPROXYLOG["backend_queue"] = requestQueueInfo[1]
      HAPROXYLOG["http_request"] = haproxyLogLineSplit[18]
      return HAPROXYLOG
