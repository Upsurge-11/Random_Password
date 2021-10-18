import random


chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+=-|/?,<>.~`"

check = 1

while check:
    pass_count = int(input("How many password options do you want :- "))
    for i in range(pass_count):
        pass_len = int(input("What should be the length of the password :- "))
        password = ""
        for j in range(pass_len):
            pass_char = random.choice(chars)
            password = password + pass_char

        print(password)

    check = int(input("Do you want to continue(0=No, 1=Yes ):-"))
