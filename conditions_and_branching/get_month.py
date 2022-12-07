# Task: Write a program to read any Month number in integer
# ...and display the Month in word.

# Define a function that holds all Months
def month(index):
    if index >= 1 and index <= 12:
        month = "December"
        if index == 1:
            month = "January"
            return month
        elif index == 2:
            month = "February"
            return month
        elif index == 3:
            month = "March"
            return month
        elif index == 4:
            month = "April"
            return month
        elif index == 5:
            month = "May"
            return month
        elif index == 6:
            month = "June"
            return month
        elif index == 7:
            month = "July"
            return month
        elif index == 8:
            month = "August"
            return month
        elif index == 9:
            month = "September"
            return month
        elif index == 10:
            month = "October"
            return month
        elif index == 11:
            month = "November"
            return month
        else:
            return month
    else:
        message = "not a month!"
        return message

# Read user input
index = int(input("Enter the month number: "))

# Call function that declares month
month_in_word = month(index)

# Display the Month in word
print("The month number, " + str(index) + " is " + month_in_word)

