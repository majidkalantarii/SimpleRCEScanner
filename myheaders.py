#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import re
import urllib
from urllib import FancyURLopener


class UserAgent(FancyURLopener):
	verion = 'Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101  Firefox/28.0'

useragent = UserAgent()


class HTTP_HEADER:
	HOST = "Host"
	SERVER = "Server"

def headersRdr(url):
	print "Basic information about the site:\n"
	opener = urllib.urlopen(url)
	if (opener.code == 200):
		print "Status: 200 - OK"
	if (opener.code == 404):
		print "Status: 404 - ERROR"
		exit()

	Server = opener.headers.get(HTTP_HEADER.SERVER)
	Host = url.split("/")[2]
	print "Host: " + str(Host)
	print "Web server: " + str(Server)

