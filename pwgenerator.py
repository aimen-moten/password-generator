print("Welcome to the CoolPw: The Ultimate Password Generator!\n")

# ASCII Value ranges:
# symbols: 33-47
# numbers: 48-57
# uppercase: 65-90
# lowercase: 97-122

import math, random
lowerLetters = int(input("How many lower case letters do you need? \n"))
upperLetters = int(input("How many upper case letters do you need?\n"))
numbers = int(input("How many numbers do you need?\n"))
symbols = int(input("How many symbols do you need?\n"))

password = ""
for i in range(lowerLetters):
    password += chr(random.randint(97,123))

for i in range(upperLetters):
    password += chr(random.randint(65,91))

for i in range(symbols):
    password += chr(random.randint(33,48))

for i in range(numbers):
    password += chr(random.randint(48,58))

pw = "".join(random.sample(password, len(password)))
print(pw)


