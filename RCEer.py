#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from myheaders import *
from myvulns import *


print ''' 
                             888 88e    e88'Y88 888'Y88 
                             888 888D  d888  'Y 888 ,'Y 
                             888 88"  C8888     888C8   
                             888 b,    Y888  ,d 888 ",d 
                             888 88b,   "88,d88 888,d88 
                                                        
                                                        
                                                                     
                dP"Y  e88'888  ,"Y88b 888 8e  888 8e   ,e e,  888,8, 
               C88b  d888  '8 "8" 888 888 88b 888 88b d88 88b 888 "  
                Y88D Y888   , ,ee 888 888 888 888 888 888   , 888    
               d,dP   "88,e8' "88 888 888 888 888 888  "YeeP" 888   
		
		Sagheb Simple RCE Scanner
		Author: Majid kalantari
        Special thanks: Instagram.com/majid_kalantarii
		This a simple but powerful RCE Scanner, if you want more
		information, please contact me at my Twitter account.
                                                                                     '''

url = raw_input("URL (ex: http://www.site.com/ping.php?ip=127.0.0.1): ")
if ("?") in url:
	RCEfunction(url)
else:
	print "Sorry, I need an URL with parameters..."
	exit()
