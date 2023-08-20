import string 

klucz = string.ascii_letters
print(klucz)

def szyfruj(word, przesuniencie):
    zaszyfrowane_slowo = ''
    for litera in word:
        nowy_index = (klucz.index(litera) + przesuniencie) % len(klucz)
        zaszyfrowane_slowo += klucz[nowy_index]
    return zaszyfrowane_slowo

def deszyfruj(word, przesuniencie):
    odszyfrowane_slowo = ''
    for litera in word:
        nowy_index = (klucz.index(litera) - przesuniencie) % len(klucz)
        odszyfrowane_slowo += klucz[nowy_index]
    return odszyfrowane_slowo

zaszyfrowane = szyfruj('adam', 3)
print(zaszyfrowane)
print(deszyfruj(zaszyfrowane, 3))