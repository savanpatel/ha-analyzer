#!/usr/bin/python

#------------------------------------------------------------------------------#
#  parses config file for ha-proxy analyzer and returns config in dictionary   #
#  Config file format: <attribute> <param1> <param2> <param3>                  #
#                                                                              #
#  @params: configFilePath                                                     #
#  @returns: dictionary [attrubute, 'config params']                           #
#  @throws:  Exception if config file is Invalid                               #
#                                                                              #
#  @author: Savan Patel                                                        #
#           savanpatel3@gmail.com                                              #
#------------------------------------------------------------------------------#

def parse(configFilePath):
      CONFIG = {}
      with open(configFilePath) as configFile:
          configs = configFile.readlines()
          for configLine in configs:
             if configLine == '\n':
                continue
             if not configLine.startswith('#'):
                if not len(configLine.split(" ", 1)) > 1:
                    raise Exception("\nInvalid line in config :" + configLine)
                CONFIG[configLine.split(" ", 1)[0]] = configLine.split(" ", 1)[1].rstrip()
      return CONFIG
