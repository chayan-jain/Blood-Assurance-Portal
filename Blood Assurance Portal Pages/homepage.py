#!/usr/bin/python2


print("content-type: text/html")
print("")


import commands as sp


print("")

print("""
<html>
<body background='IMG1.jpg'>
<form action='user_check.py'>
<center>
<h1><u>Welcome to Blood Assurance Portal</u></h1>
<h3>Login as General user</h3>
UserName:-\t<input type='text' name='un' />
</br>
Password:-\t<input type='password' name='passwd' />
</br>
</br>
<input type='submit' name='s' />

</center>
</form>
</body>
</html>
""")

print("""
<h3></h3>
</br>
<a target='diframe' href='admin_login.py'>Login as admin user</a>

&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp

<a  target='diframe1' href='new_user.py'>Create new User</a>
<br/>
<iframe width=45% height=40% name='diframe' ></iframe>
<iframe width=45% height=40% name='diframe1' ></iframe>
""")





