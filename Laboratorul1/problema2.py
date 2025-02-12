import random

Σ1 = list("0123456789")
Σ2 = list("abcdefgijk")
Σ3 = ["x1", "y1", "x2", "y2", "x3", "y3", "x4", "y4", "x5", "y5"]
simboluri = [Σ1, Σ2, Σ3]

def random_cuvant():
    return "".join(random.choice(random.choice(simboluri)) for _ in range(random.randint(3, 7)))

def fun(cuvant,n):
    i, j = sorted(random.sample(range(len(cuvant)), 2))
    cuvant_i = cuvant
    concatenare= cuvant + cuvant
    cuvant= concatenare
    repetare = cuvant*n
    cuvant = repetare
    inversare = cuvant[::-1]
    cuvant = inversare
    extractie = cuvant[i:j+1]
    cuvant = extractie
    inlocuire = cuvant[:i] + random.choice(Σ1 + Σ2 + Σ3) + cuvant[i+1:] if cuvant else cuvant
    return {
        "Cuvânt inițial": cuvant_i,
        "Concatenare": concatenare,
        "Repetare": repetare,
        "Inversare": inversare,
        "Extracție": extractie,
        "Înlocuire": inlocuire
    }

cuvant_random = random_cuvant()
rezultate = fun(cuvant_random,5)

for operatie, rezultat in rezultate.items():
    print(f"{operatie}: {rezultat}")
