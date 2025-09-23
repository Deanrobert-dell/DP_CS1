#DP 2nd grade check
grade = float(input("what is your grade as a percentage (dont include percent symbol): "))

if grade >=93:
    print ("you have an A good job")
elif grade >=90 and grade < 93:
    print ("you have an A- so close")
elif grade >=87 and grade < 90:
    print ("you have a B+ very good")
elif grade >=83 and grade <87:
    print ("you have a B, your average")
elif grade >= 80 and grade <83:
    print ("you have a B- just below average")
elif grade >=77 and grade <80:
    print ("you have C+, at least it's a plus")
elif grade >=73 and grade <77:
    print ("you have a C, do your homework")
elif grade >=70 and grade <73:
    print ("you have a C-, you are cooked")
elif grade >= 67 and grade <70:
    print ("you have a D+, so close... to a C ")
elif grade >= 63 and grade <67:
    print ("you have a D, horrible")
elif grade >= 60 and grade <63:
    print ("you have a D-, say goodbye to college")
else:
    print ("you have an F, failing")