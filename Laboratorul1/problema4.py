def generare(max_lungime):
    cuvinte = {""}  
    rezultat = set(cuvinte)  

    for _ in range(max_lungime):
        cuvinte = {cuv + litera for cuv in cuvinte for litera in "ab"}
        rezultat.update(cuvinte)  

    return sorted(rezultat, key=lambda x: (len(x), x))

max_lungime = 4  
cuvinte = generare(max_lungime)

print("Cuvinte generate:")
print(" ".join(cuvinte))
