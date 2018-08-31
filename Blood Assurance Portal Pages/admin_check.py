#!/usr/bin/python2


print("content-type: text/html")
print("")


import commands as sp
import cgi

#form = cgi.FieldStorage()
#choice = cgi.getvalue('ch')

print("""
<h3><center><u>How can i help you:- </u></center></h3>
<form action='operation_sql.py'>
Insert Data  &nbsp&nbsp <input type='radio' name='ch' /> 
</br>
Delete Data &nbsp&nbsp&nbsp&nbsp <input type='radio' name='ch'/>
&nbsp&nbsp&nbsp&nbsp
</br>
Update Data &nbsp&nbsp&nbsp&nbsp <input type='radio' name='ch'/>
</br>
Generate Analyse Report <input type='radio' name='ch'/>
</br>
Generate Prediction Report <input type='radio' name='ch'/>
</br>
</br>
</br>
<input type='submit' name='s3' />
</form>
""")

