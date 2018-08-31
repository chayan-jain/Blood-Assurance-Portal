#!/usr/bin/python2


print("content-type: text/html")
print("")


import commands as sp
import cgi

form = cgi.FieldStorage()
operation = form.getvalue('ch')

print("This Page is for future use.")
print("Please Visit the Windows OS for output.")


#Hadoop service start

if operation=="Insert":
	print('insert')
	pass
elif operation=="Delete":
	print('delete')
	pass
elif operation=="Update":
	print('update')	
	pass 
elif operation=="Analyse":
	print('analysed report')
  	pass
elif operation=="Prediction":
	print('prediction report')
	pass


