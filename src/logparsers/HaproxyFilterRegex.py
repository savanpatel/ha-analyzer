#!/usr/bin/python
import re

#------------------------------------------------------------------------------#
#  provides regular expression for haproxy log filtering                       #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#  @author: Savan Patel                                                        #
#           savanpatel3@gmail.com                                              #
#------------------------------------------------------------------------------#

def getHaproxyFilterRegex():
    re1='((?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Sept|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?))'	# Month 1
    re2='(\\s+)'	# White Space 1
    re3='((?:(?:[0-2]?\\d{1})|(?:[3][01]{1})))(?![\\d])'	# Day 1
    re4='(\\s+)'	# White Space 2
    re5='(\\d)'	# Any Single Digit 1
    re6='(\\d)'	# Any Single Digit 2
    re7='(.)'	# Any Single Character 1
    re8='(\\d)'	# Any Single Digit 3
    re9='(\\d)'	# Any Single Digit 4
    re10='(.)'	# Any Single Character 2
    re11='(\\d)'	# Any Single Digit 5
    re12='(\\d)'	# Any Single Digit 6
    re13='(\\s+)'	# White Space 3
    re14='((?:[a-z][a-z]+))'	# Word 1
    re15='(\\s+)'	# White Space 4
    re16='((?:[a-z][a-z]+))'	# Word 2
    re17='(\\[.*?\\])'	# Square Braces 1
    re18='(.)'	# Any Single Character 3
    re19='(.)'	# Any Single Character 4
    re20='((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))(?![\\d])'	# IPv4 IP Address 1
    re21='(.)'	# Any Single Character 5
    re22='(\\d+)'	# Integer Number 1
    re23='(.)'	# Any Single Character 6
    re24='(.)'	# Any Single Character 7
    re25='((?:(?:[0-2]?\\d{1})|(?:[3][01]{1})))(?![\\d])'	# Day 2
    re26='(.)'	# Any Single Character 8
    re27='((?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Sept|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?))'	# Month 2
    re28='(.)'	# Any Single Character 9
    re29='(\\d+)'	# Integer Number 2
    re30='.*?'	# Non-greedy match on filler
    re31='(\\d+)'	# Integer Number 3
    re32='.*?'	# Non-greedy match on filler
    re33='(\\d+)'	# Integer Number 4
    re34='.*?'	# Non-greedy match on filler
    re35='(\\d+)'	# Integer Number 5
    re36='.*?'	# Non-greedy match on filler
    re37='((?:[a-z][a-z]+))'	# Word 3
    re38='.*?'	# Non-greedy match on filler
    re39='(?:[a-z][a-z]+)'	# Uninteresting: word
    re40='.*?'	# Non-greedy match on filler
    re41='((?:[a-z][a-z]+))'	# Word 4
    re42='.*?'	# Non-greedy match on filler
    re43='(?:[a-z][a-z]+)'	# Uninteresting: word
    re44='.*?'	# Non-greedy match on filler
    re45='(?:[a-z][a-z]+)'	# Uninteresting: word
    re46='.*?'	# Non-greedy match on filler
    re47='(?:[a-z][a-z]+)'	# Uninteresting: word
    re48='.*?'	# Non-greedy match on filler
    re49='(?:[a-z][a-z]+)'	# Uninteresting: word
    re50='.*?'	# Non-greedy match on filler
    re51='(?:[a-z][a-z]+)'	# Uninteresting: word
    re52='.*?'	# Non-greedy match on filler
    re53='((?:[a-z][a-z]+))'	# Word 5
    re54='.*?'	# Non-greedy match on filler
    re55='((?:[a-z][a-z]+))'	# Word 6
    re56='.*?'	# Non-greedy match on filler
    re57='((?:[a-z][a-z]+))'	# Word 7

    rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8+re9+re10+re11+re12+re13+re14+re15+re16+re17+re18+re19+re20+re21+re22+re23+re24+re25+re26+re27+re28+re29+re30+re31+re32+re33+re34+re35+re36+re37+re38+re39+re40+re41+re42+re43+re44+re45+re46+re47+re48+re49+re50+re51+re52+re53+re54+re55+re56+re57,re.IGNORECASE|re.DOTALL)
    return rg
