import random

chars = '&()-_@,?;./:!§$%*ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'


number = input('How much password ? ')
number = int(number)

length = input('Password length ? ')

length = int(length)

for p in range(number):
    password = ' '
    for c in range(length):
        password += random.choice(chars)
    print(password)