import string 

klucz = string.ascii_letters
print(klucz)

def szyfruj(word, przesuniencie):
    zaszyfrowane_slowo = ''
    for litera in word:
        nowy_index = (klucz.index(litera) + przesuniencie) % len(klucz)
        zaszyfrowane_slowo += klucz[nowy_index]
    return zaszyfrowane_slowo

print (szyfruj('zoo', 3))
