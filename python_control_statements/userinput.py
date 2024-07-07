# Ask user to enter two integer values
n1, n2 = input('Enter 2 values: ').split()

# Covert strings into regular numbers
n1 = int(n1)
n2 = int(n2)

# Add the values
sum = n1 + n2

# Subtract the values
sum1 = n1 - n2

# Multiply the values
product = n1 * n2

# Divide the values
quotient = n1 / n2

# Find remainder of the values
remainder = n1 % n2

# Print the values in a formated way
print("{} + {} = {}".format(n1, n2, sum))
print("{} - {} = {}".format(n1, n2, sum1))
print("{} * {} = {}".format(n1, n2, product))
print("{} / {} = {}".format(n1, n2, quotient))
print("{} % {} = {}".format(n1, n2, remainder))
