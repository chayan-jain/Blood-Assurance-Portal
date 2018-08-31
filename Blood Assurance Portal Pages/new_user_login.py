#!/usr/bin/python2


print("content-type: text/html")
print("")


import commands as sp


print("""
<form action='user_insert.py'>
<center> <u> Please fill the following details :-> </center> </u> </br>
<hr>
<div >
UserID:-       <input type='text' name='uId' /> </br>
Password:-       <input type='password' name='pwd' /> </br>
Name:-         <input type='text' name='name' /> </br>
Contact No.:-  <input type='text' name='conNo'/> </br>
Blood Group:- </br> </br>
A+  <input type='radio'  name='bg' value='A+' /> 
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
A-  <input type='radio'  name='bg' value='A-' />
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp 
B+  <input type='radio'  name='bg' value='B+' /> 
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp 
B-  <input type='radio'  name='bg' value='B-' /> 
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp </br>
AB+  <input type='radio'  name='bg' value='AB+' /> 
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp 
AB-  <input type='radio'  name='bg' value='AB-' /> 
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp 
O+ <input type='radio'  name='bg' value='O+'/> 
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp 
O- <input type='radio'  name='bg' value='O- /> 
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp 
HH  <input type='radio'  name='hh' value='HH' /> </br> </br>
Location:-  <input type='text' name='city'/> </br>
Age:-  &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp <input type='text' name='age' /> </br></br>
Eligible to donate blood:- </br>
Yes<input type='radio'  name='elig' value='yes'/> 
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp 
No<input type='radio'   name='elig' value='no' /> </br>
</br>
Fingerprint:-  <input type='file' name='fing' accept='image' /> </br>
</br>
<center><input type='submit' name='s' /></center>
</div>
<hr>
</form>
""")























