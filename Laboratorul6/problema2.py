import itertools

def citeste_limbaj(nr):
    limbaj = input(f"Introdu limbajul {nr} (elementele separate prin virgulă, ex: ab,ba): ")
    return set(limbaj.split(","))

def reuniune(l1, l2):
    return l1 | l2

def intersectie(l1, l2):
    return l1 & l2

def concatenare(l1, l2):
    return {x + y for x, y in itertools.product(l1, l2)}

def diferenta(l1, l2):
    return l1 - l2

def diferenta_simetrica(l1, l2):
    return (l1 - l2) | (l2 - l1)


def afiseaza_meniu():
    print("\nSelectează operația:")
    print("1 - Reuniune")
    print("2 - Intersecție")
    print("3 - Concatenare")
    print("4 - Diferență")
    print("5 - Diferenta Simetrica")
    print("0 - Ieșire")

def main():
    print("Aplicație pentru Operații pe Limbaje Regulate\n")
    l1 = citeste_limbaj(1)
    l2 = citeste_limbaj(2)
    
    while True:
        afiseaza_meniu()
        optiune = input("Alege o opțiune: ")
        
        if optiune == "1":
            print("Reuniune:", reuniune(l1, l2))
        elif optiune == "2":
            print("Intersecție:", intersectie(l1, l2))
        elif optiune == "3":
            print("Concatenare:", concatenare(l1, l2))
        elif optiune == "4":
            print("Diferență L1 - L2:", diferenta(l1, l2))
        elif optiune == "5":
             print("Diferență Simetrică:", diferenta_simetrica(l1, l2))
        elif optiune == "0":
            print("Ieșire...")
            break
        else:
            print("Opțiune invalidă!")

if __name__ == "__main__":
    main()