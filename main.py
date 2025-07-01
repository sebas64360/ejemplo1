import random

chart = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

leng = int(input("Ingresa la longitud de la contraseña:"))

password = ""

for i in range(leng):
    password = password  + random.choice(chart)

print(password)