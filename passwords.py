import random
import string


print("\nMY PASSWORD GENERATOR")
print("**********************\n")

# A password should contain lowercase letters
# uppercase letter, numbers and symbols
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase

numbers = ''.join([str(x) for x in range(10)])
allowed_symbols = '!@#$%^&*().,?'


# Password characters to choose from
password_characters = lowercase_letters + uppercase_letters + numbers + allowed_symbols


# Record user input
number_of_passwords = int(input("Enter the number of passwords to generate: "))
password_length = int(input("Enter the desired password length: "))
print("\nSee the passwords below:")


for password_counter in range(number_of_passwords):
	password = ""

	for character_counter in range(password_length):
		password += random.choice(password_characters)

	print(password)

# The program does not have any password patterns enforced
# e.g. Must have atleast one uppercase letter, one lowercase letter
# a number and a symbol
# Program can be improved by enforcing patterns
