import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []
print("Welcome to the Password Generator!")
let = int(input('How many letters would you like in your password?: '))
sym = int(input('How many symbols would you like?: '))
num = int(input('How many numbers would you like?: '))
for l in range(0, let):
    password.append(random.choice(letters))

for s in range(0, sym):
    password.append(random.choice(symbols))

for n in range(0, num):
    password.append(random.choice(numbers))
random.shuffle(password)
''.join(map(str, password))
print(*password, sep='')
