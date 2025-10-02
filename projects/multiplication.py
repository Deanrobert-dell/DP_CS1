table = [1,2,3,4,5,6,7,8,9,10,11,12]

for item in table:
    row = ""
    for i in table:
        row = row + str(item * i) + ' '  # concatinates spaces betwen numbers
    print(row)  # prints the row that i created
