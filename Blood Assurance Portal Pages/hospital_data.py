#!/usr/bin/python2


print("content-type: text/html")
print("")


import commands as sp



print("""
<form action='http://192.168.43.55/cgi-bin/project/project/homepage.py' />
<center> <u>Enter the details of hospital </u></center>
<hr>
Name of Hospital :- &nbsp&nbsp&nbsp&nbsp<input type='text' name='h' />
<br/>
Name of Doctor :- &nbsp&nbsp&nbsp&nbsp&nbsp <input type='text' name='d1' />
<br/>
Fingerprint :- 
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp <input type='file' name='fp' accept='image' />
<br/>
Mobile No :- 
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp <input type='text' name='mn' />
<br/>
<br/>
Name of Doctor :- 
&nbsp&nbsp&nbsp&nbsp&nbsp <input type='text' name='d2' />
<br/>
Fingerprint :- 
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<input type='file' name='fp1' accept='image' />
<br/>
Mobile No :- 
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<input type='text' name='mn1' />
<br/>
<center><input type='submit' name='s'/></center>
<hr>
</form>
""")
