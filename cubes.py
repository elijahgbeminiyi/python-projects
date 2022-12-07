# Defining the function to calculate the cube
def cubes(start, end):
    for i in range(start, end +1):
        print("{} x {} x {} = {}".format(i, i , i, i ** 3))

#Get user starting point
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Calling the function
cubes(start, end)
