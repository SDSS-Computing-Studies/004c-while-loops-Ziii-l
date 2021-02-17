#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied
"""
username = "admin"
password =12345

while username == "admin" and password == 12345:
    username=str(input("please enter username"))
    if username== "admin":
        print("Access granted")
    password=str(input("please enter password"))
    if password == "12345":
        print("Access denied")
