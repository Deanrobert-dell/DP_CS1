#DP 2nd user sign-in

#asks user for username and password
username = input ("enter username: ")
login = input ("enter password: ")

#checks if username and password matches if they dont, then dont sign in
if username == "dean" and login == "12345":
    print ("signing in...")
elif username == "dean" and login != "12345":
    print ("wrong password... retry")
else:
    print ("login failed")
