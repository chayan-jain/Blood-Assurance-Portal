#!/usr/bin/python2

print("content-type: text/html")
print("")


import commands as sp

   

print("""
<form action='operation_sql.py' >
insertdata<input type='radio' name='ch' value='insert' />
</br>
updatedata<input type='radio' name='ch' value='update' />
</br>
deletedata<input type='radio' name='ch' value='delete' />
</br>
Generate Analysed report<input type='radio' name='gar' value='generate' />
</br>
Generate Prediction report<input type='radio' name='gpr' value='prediction' />
</br>
submit<input type='submit' name='c' />
</form>
""")


#print("iframe <a href='operation_sql.py'> Click here to start operation  </a>")
