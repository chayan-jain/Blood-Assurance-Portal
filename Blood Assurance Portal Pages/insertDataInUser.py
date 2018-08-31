#!/usr/bin/python2

import subprocess
import cgi
import cgitb
import sqlite3

cgitb.enable()


print("content-type: text/html")
print("")

form = cgi.FieldStorage()
name = form.getvalue('n')
contactNo = form.getvalue('c')
bloodgroup = form.getvalue('bg')
loc = form.getvalue('l')
age = form.getvalue('ag')
eligible = form.getvalue('e')
fingerprint = form.getvalue('fing')


#Storing Data into database
conn = sqlite3.connect("BloodDatabase.db")
print(conn)
print "Opened database successfully";


conn.execute("INSERT INTO HOSPITAL (ID,NAME,AGE,ADDRESS,CONTACT_NO,BLOOD_GROUP,ELIGIBILITY,FINGERPRINT) \
	VALUES (8, 'Chayan', 21, 'Jaipur',9462626321,'O+','Yes','FILE' )");

conn.commit()
print "Records created successfully";
conn.close()


print(name,contactNo,bloodgroup,loc,age,eligible,fingerprint)
print("Hi")
