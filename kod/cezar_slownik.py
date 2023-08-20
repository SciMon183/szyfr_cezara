import string 

alfabet = string.ascii_letters
print(alfabet)
print()

def szyfruj(word, przesuniencie):

    klucz = {}
    for litera in alfabet:
        nowy_index = (alfabet.index(litera) + przesuniencie) % len(alfabet)
        klucz [litera] = alfabet[nowy_index]

    zaszyfrowane_slowo = ''
    for litera in word:
        zaszyfrowane_slowo += klucz[litera]
         
    return zaszyfrowane_slowo

def deszyfruj(word, przesuniencie):

    klucz = {}
    for litera in alfabet:
        nowy_index = (alfabet.index(litera) + przesuniencie) % len(alfabet)
        klucz [alfabet[nowy_index]] = litera

    zaszyfrowane_slowo = ''
    for litera in word:
        zaszyfrowane_slowo += klucz[litera]
         
    return zaszyfrowane_slowo


zaszyfrowane = szyfruj('adam', 3)
print(zaszyfrowane)
print(deszyfruj(zaszyfrowane, 3))