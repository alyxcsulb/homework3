# Change in cents output
# (Calculate change using fewest number of coins)

change = int(input("Enter amount of change due in cents: "))
print("Your change is: ")
print(change//25, "quarters")
change = change%25
print(change//10, "dimes")
change = change%10
print(change//5, "nickels")
change = change%5
print(change//1, "pennies")
change = change%1
