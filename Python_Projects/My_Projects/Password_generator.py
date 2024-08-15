import string
import random

# Empty list
password = []

# Convert uppercase alphabet into a list
uppercase_string = string.ascii_uppercase
uppercase = list(uppercase_string)

# Convert lowercase alphabet into a list
lowercase_string = string.ascii_lowercase
lowercase = list(lowercase_string)

# Clearing the list - gives new password everytime this is run
password *= 0

# Generate a 12 character password and add to empty list
while len(password) < 12:
    password.append(random.choices(uppercase)) or password.append(random.choices(lowercase)) or password.append(random.randint(0, 9))
    
print(password)
