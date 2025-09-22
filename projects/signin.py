#DP 2nd user sign-in
username = input ("enter username: ")
login = input ("enter password: ")
if username == ("dean") and login == ("12345"):
    print ("signing in...")
elif username == ("dean") and login != ("12345"):
    print ("wrong password... retry")
else:
    print ("login failed")
