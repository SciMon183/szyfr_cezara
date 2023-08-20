klucz = "abcdefghijklmnopqrstuwxyz"

litera = 'a' 

def szyfruj(litera, przesuniencie):
    
    nowy_index = klucz.index(litera) + przesuniencie
    return klucz[nowy_index]


print (szyfruj('b', 3))
