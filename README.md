# ha-analyzer
parse haproxy logs and store to db for analysis.

# How
ha-analyzer parses for the haproxy logs and stores in mysql db. Please read WIKI for setting up and running ha-analyzer.
###haproxy-analyzer
  haproxy-analyzer  mines  haproxy logs  and  stores 
  them into database.  Later  they  can  be analyzed 
  against type of request, response code, time taken 
  etc parameters.

###ha-ui
  the  ha-ui  mines  data  from  the  database
  and gives  various  view  for  the  requests.

#Wiki
 https://github.com/savanpatel/ha-analyzer/wiki
 
#Prerequisite
 python modules: 
   os
   sys
   subprocess
   logging
#ToDo
  build UI for the trends.
  

#Contributors: 
### Savan Patel (savanpatel3@gmail.com)
          

Please read the WIKI to configure haproxy-analyzer.
