name = input("What is your name: ").strip().title()
pnumber = input ("what is your phone number: ").strip()
gpa = input("what is your gpa: ").strip()
word = "-"
name_nospaces = name.replace(" ", "")
print(name_nospaces)
print(pnumber.replace(word, ' '))




if (gpa).isnumeric():
    print (gpa)
else: 
    print ("put in numerical data for gpa")

