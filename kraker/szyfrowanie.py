import string 

# --------------------------------szyfrowanie proste nadawca -------------------------------

plain_text = "hello world"          # wiadomość do zaszyfrowanie 
shift = 80                           # jakie przesunięcie wybierasz
shift %= 26

alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]

table = str.maketrans(alphabet, shifted)

encrypted = plain_text.translate(table)

print(encrypted)

# --------------------------------deszyfrowanie proste odbiorca -------------------------------

plain_text = "jgnnq yqtnf"          # wiadomość do oszyfrownia  
shift = 26 - 80                           # rzeby deszyfrować podaj 26 - "twój klucz od nadawcy"
shift %= 26

alphabet = string.ascii_letters
shifted = alphabet[shift:] + alphabet[:shift]

table = str.maketrans(alphabet, shifted)

crypted = plain_text.translate(table)

print(crypted)