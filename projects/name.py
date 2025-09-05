#DP 2nd idiotproof
name = input("What is your name: ").strip().capitalize()
last_name = input ("what is your last name: ").strip().capitalize()
pnumber = input ("what is your phone number: ").strip()
gpa = input("what is your gpa: ").strip()
word = "-"
fixedpnumber = pnumber.replace(word, ' ')
gpa_nospaces = gpa.replace(" ", "")
name_nospace = name.replace(" ", "")
last_name_nospace = last_name.replace(" ", "")


print("hello " + name_nospace +" "+ last_name_nospace + " your number is " + fixedpnumber + " your gpa is " + gpa_nospaces)
