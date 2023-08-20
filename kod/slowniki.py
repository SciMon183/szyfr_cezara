slownik = {'adam' : 32, 'marek' : 40}

slownik['wojtek'] = 60
print(slownik.get('wojtekk'))

for klucz in slownik:
    print(klucz)

for warotsci in slownik.values():
    print(warotsci)

for wszystko in slownik.items():
    print(wszystko)
