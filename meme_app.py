import time
meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "SHEESH": "Yok artik",
            "GG": "Iyi oyunlar",
            }


word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print("Kelimenin anlami:", meme_dict[word])
else:
    print("Bu kelimeyi bilmiyorum!")
    time.sleep(1)
    ekle = input("Bu kelimeyi listeye eklemeyi istiyormusun? (hepsini büyük harflerle yazın!)")
    if ekle == "EVET":
        meme_dict[word] = "deger"
