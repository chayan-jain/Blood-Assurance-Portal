#!/usr/bin/python2

import cgi

print("content-type: text/html")
#print("")

form = cgi.FieldStorage()
name = form.getvalue('user')

#print(name)
#print("Hi")

if name=="Public":
	print("location: http://192.168.43.55:80/cgi-bin/project/project/new_user_login.py")
	print("")
elif name=="Hospital":
	print("location: http://192.168.43.55:80/cgi-bin/project/project/hospital_data.py"
	print("")

