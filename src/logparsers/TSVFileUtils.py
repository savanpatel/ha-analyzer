#!/usr/bin/python

#------------------------------------------------------------------------------#
#  provides tsv file utils                                                     #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#  @author: Savan Patel                                                        #
#           savanpatel3@gmail.com                                              #
#------------------------------------------------------------------------------#



#convert haproxy stats info from dictionary to tsv and store to file
def pushToTSVFile(HAPROXYLOG, tsvfilepath):
    tsvLine = HAPROXYLOG["date"] + "\t" + HAPROXYLOG["processnamepid"] + "\t" + HAPROXYLOG["clientip"] + "\t" + HAPROXYLOG["clientport"]
    tsvLine = tsvLine + "\t" + HAPROXYLOG["accept_date"] + "\t" + HAPROXYLOG["frontend_listener"]
    tsvLine = tsvLine + "\t" + HAPROXYLOG["backend_name"] + "\t" + HAPROXYLOG["server_name"]
    tsvLine = tsvLine + "\t" + HAPROXYLOG["Tq"]+ "\t" + HAPROXYLOG["Tw"]+ "\t" + HAPROXYLOG["Tc"]+ "\t" + HAPROXYLOG["Tr"]+ "\t" + HAPROXYLOG["Tt"]
    tsvLine = tsvLine + "\t" + HAPROXYLOG["status_code"]
    tsvLine = tsvLine + "\t" + HAPROXYLOG["ac"] + "\t" + HAPROXYLOG["fc"] + "\t" + HAPROXYLOG["bc"] + "\t" + HAPROXYLOG["sc"] + "\t" + HAPROXYLOG["rc"]
    tsvLine = tsvLine + "\t" + HAPROXYLOG["srv_queue"] + "\t" + HAPROXYLOG["backend_queue"] + "\t" + HAPROXYLOG["http_request"]

    with open(tsvfilepath, "a") as tsvFile:
       tsvFile.write(tsvLine + "\n")
