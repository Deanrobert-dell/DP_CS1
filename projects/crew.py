# DP 2nd crew shares

# Ask inputs
money = float(input("What was the money earned in dollars: "))
members = int(input("How many crew members are there (besides captain and first mate): "))

# Total shares: 
total_shares = 7 + 3 + members

# money in one share
share = money / total_shares

# money owed
captain_Money = 7 * share
firstmate = 3 * share
crew_Total = members * share

#outputs
print("Captain gets", round(captain_Money, 2))
print("First mate gets", round(firstmate, 2))
print("crew still needs ", round(crew_Total, 2))
print ("each crew member gets ", round(crew_Total / members, 2))


