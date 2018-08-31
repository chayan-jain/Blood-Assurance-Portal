#!/usr/bin/python2

print("content-type: text/html")
print("")

import commands as sp
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
uId = form.getvalue('uId')
pwd = form.getvalue('pwd')
name = form.getvalue('name')
city = form.getvalue('city')
elig = form.getvalue('elig')
age = form.getvalue('age')
bg = form.getvalue('bg')
conNo = form.getvalue('conNo')


string = ("{},{},{},{},{},{},{},{}\n".format(name,city,elig,age,bg,conNo,uId,pwd))

with open('userDetails.csv','a') as b:
	b.write(string)
	
print("<center> <h3> Updated Successfully </h3> </center>")

print("""
<form action='http://192.168.43.55/cgi-bin/project/project/homepage.py'>
	<input type='submit' value='Home page' />
</form>
""")
