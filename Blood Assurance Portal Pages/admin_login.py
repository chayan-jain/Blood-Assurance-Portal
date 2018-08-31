#!/usr/bin/python2


print("content-type: text/html")
print("")


import commands as sp



print("""
<h3><u>Admin Login Portal</u></h3>
<form action='admin_check.py' target='_blank'>
Facial Recognition &nbsp&nbsp <input type='radio' name='ch' />
</br>
Access Password &nbsp&nbsp&nbsp&nbsp <input type='radio' name='ch'/>
&nbsp&nbsp&nbsp&nbsp
<input type='password' name='password' placeholder='Enter password'/>
</br>
</br>
<input type='submit' name='s3' />
</form>
""")

