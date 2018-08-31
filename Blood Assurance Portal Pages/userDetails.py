#!/usr/bin/python2

print("content-type: text/html")
print("")


import cgi
#import cgit

#cgit.enable()
form = cgi.FieldStorage()
bg = form.getvalue('bg')
city = form.getvalue('city')

with open('userDetails.csv','r') as b:
	for x in b.readlines():
		f = x.strip('\n').split(',')
		if f[1]==city and f[4]==bg and (f[2]=='Yes' or f[2]=='yes'):
			print("""
			Name:- {} </br>
			Contact-Number:- {} </br></br>
			""").format(f[0],f[5]) 
print("""
<form action='http://192.168.43.55/cgi-bin/project/project/homepage.py'>
<input type='submit' value='Go to Home page' />
""")
fp.close()

