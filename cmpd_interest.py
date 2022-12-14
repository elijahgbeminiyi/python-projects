# Have the user enter their investment amount and expected interest
# Each year their investment will increase by their invenstment + their investment * interest rate is
# Print out the earnings after a 10 year period

# Ask for the money invested + the interest rate
money = input("Enter amount to be invested: ")
interest = input("Enter interest rate: ")

# Convert the value to a float
money = float(money)

# Convert the value to a float and round the percentage rate by 2 digits
interest = float(interest) * .01

# Cycle through 10 years using a for loop and range from 0 to 9
for i in range(10):
    money = money + (money * interest)

# Output the results
print("Investment after 10 years: {:.2f}".format(money))
