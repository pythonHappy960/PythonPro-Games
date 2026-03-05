import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk = int(input("parolanizin uzunlugu kac olsun?"))

parola = ""

for i in range(uzunluk):
    karakter = random.choice(karakterler)
    parola += karakter

print("Parolaniz:", parola)
