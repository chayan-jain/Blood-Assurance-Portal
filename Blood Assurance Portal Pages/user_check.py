#!/usr/bin/python2

print("content-type: text/html")

import commands as sp
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
userId = form.getvalue('un')
password = form.getvalue('passwd')
flag = 0
with open('userDetails.csv','r') as b:
	for x in b.readlines():
		f = x.strip('\n').split(',')
		if f[6]==userId and f[7]==password:
			print("")
			print("<h3><u> <center> Your Contact details </center> </h3></u> <hr>")
			print("Name:- {} </br>".format(f[0]))
			print("City:- {} </br>".format(f[1]))
			print("Eligibility:- {} </br>".format(f[2]))
			print("	Age:- {} </br>".format(f[3]))
			print("	Blood Group:- {} </br>".format(f[4]))
			print("	Contact Number:- {} </br>".format(f[5]))
			flag = 1
			break
if flag==0:
	print('location: http://192.168.43.55/cgi-bin/project/project/homepage.py')
	print("")
else:
	print("""
	</br></br><hr>
	<h3><center><u>Want to know the donors of :-" </u></center></h3>
	<hr>
	""")

	print("""
	<form action="userDetails.py">
	Blood-Group :- <input type='text' name='bg'/>
	</br>
	City:- <input type='text' name='city'/>
	</br>
	<a href='http://192.168.43.55/cgi-bin/project/project/userDetails.py' target='BloodUsers'><input type='submit' /> </a>
	</br>
	</form>""")
	#Search your Blood group users in your city </br>")
	#print("<iframe name='BloodUsers'> </iframe>")
