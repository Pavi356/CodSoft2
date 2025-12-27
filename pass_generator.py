import random
print("Password Generator!")
length = int(input("Enter password length: "))
incl_upper = input("Include Uppercase Letters? (yes/no): ").lower() == "yes"
incl_nums = input("Include Numbers? (yes/no): ").lower() == "yes"
incl_sybs = input("Include Symbols? (yes/no): ").lower() == "yes"
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()-_=+?/<>"
var = lowercase
if incl_upper:
    var += uppercase
if incl_nums:
    var += numbers
if incl_sybs:
    var += symbols
password = ""
for i in range(length):
    password += random.choice(var)
print("Your Generated Password is:")
print(password)
print("\n__Password Generated Successfully__!")
