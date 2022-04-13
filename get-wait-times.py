#!/usr/bin/python

import urllib2
from bs4 import BeautifulSoup
import re
import datetime
import requests

page = requests.get("https://www.dublinairport.com/flight-information/live-departures")
logtime = datetime.datetime.now()

soup = BeautifulSoup(page.content, 'html.parser')
thislist = list(())
for string in soup.body.main.div.div.stripped_strings:
	thislist.append(string.encode("utf-8"))

s1 = str(logtime.strftime("%x %X") +","+ thislist[2] +" " + thislist[3] +","+ thislist[5] +" "+ thislist[6] + "\n")

f = open("wait_times.log", "a")
f.write(s1)
f.close()
