

def cezar(co_do_zdekodowania, przesuniencie):
    done = ''
    for znak in co_do_zdekodowania:
        kodASCII = ord(znak)
        kodASCII += przesuniencie
        while kodASCII > 126:
            kodASCII -= 95 
        while kodASCII < 32:
            kodASCII += 95
        done += chr(kodASCII)
    return done

# kandytad_1 = int(input("Podaj kod do deszyfracji: "))
kandydat_2 = "/<V5;)j6\\<Y)8><\\9Fbu,Hy4ONC}pxP\"4st12wn'?@O$6BgQo7i#gtD|s>3lf="

for przesuniencie in range(-100, 101):
    print(str(przesuniencie) + " " + cezar(kandydat_2, przesuniencie))

        