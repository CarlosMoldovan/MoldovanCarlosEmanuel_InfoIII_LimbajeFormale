def concatenare(sir1,sir2):
    return sir1+sir2

def invers(sir):
    return sir[::-1]

def subs(sir,a,b):
    return [b if elem == a else elem for elem in sir]

def lungime(sir):
    return len(sir)

A = ["a", "b", "c"]
B = ["x", "y", "z"]
C = ["1", "2", "3"]

print(concatenare(A,B))
print(invers(A))
print(subs(B, "x", "c"))
print(lungime(C))

