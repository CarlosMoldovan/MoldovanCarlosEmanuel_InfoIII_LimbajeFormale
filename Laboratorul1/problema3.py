def is_palindrom(sir):
    return sir == sir[::-1]

def palindroame(alfabet, lungime, sir=""):
    if len(sir) == lungime:
        if is_palindrom(sir):
            print(sir)
        return
    
    for caracter in alfabet:
        palindroame(alfabet, lungime, sir + caracter)

alfabet = ["0", "1", "2"]

for lungime in range(1, 6):
    print(f"Lungime {lungime}:")
    palindroame(alfabet, lungime)
    print()
