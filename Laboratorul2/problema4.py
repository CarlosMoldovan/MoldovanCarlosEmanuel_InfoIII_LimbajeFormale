import re

def start(file_path):
    client_p = re.compile(r"^Client: [A-Z][a-z]+ [A-Z][a-z]+$")
    produs_p = re.compile(r"^Produs: [\w\s]+, Pret: \d+(\.\d{2})?, Cantitate: \d+$")
    tva_p = re.compile(r"^TVA: \d{1,2}%$")
    
    erori = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
            for i, line in enumerate(lines, start=1):
                line = line.strip()
                if not (client_p.match(line) or produs_p.match(line) or tva_p.match(line)):
                    erori.append(f"Linia {i} nu respectă formatul: {line}")
        
        if erori:
            print("Erori găsite în fișier:")
            for error in erori:
                print(error)
        else:
            print("Fișierul respectă formatul specificat.")
    except FileNotFoundError:
        print("Fișierul nu a fost găsit. Verificați calea și încercați din nou.")

path = input("Introduceți calea către fișierul text: ")
start(path)
