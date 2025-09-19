import random
caratteri = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
lunghezza = int(input("quanto deve essere lunga la password?"))
password = ""
for i in range(lunghezza):
    random.choice(caratteri)
    password = password + random.choice(caratteri)
print(password)
