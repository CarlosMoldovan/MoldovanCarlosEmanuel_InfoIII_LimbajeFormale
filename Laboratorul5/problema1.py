class Mealy:
    def __init__(self):
        self.stare = "S0"

    def tranzitie(self, a, b):
        if self.stare == "S0":
            if (a, b) == (0, 0):
                return "S0", 0
            elif (a, b) == (0, 1):
                self.stare = "S1"
                return "S1", 1
            elif (a, b) == (1, 0):
                return "S0", 0
            elif (a, b) == (1, 1):
                self.stare = "S1"
                return "S1", 1
        elif self.stare == "S1":
            if (a, b) == (0, 0):
                return "S1", 1
            elif (a, b) == (0, 1):
                return "S1", 1
            elif (a, b) == (1, 0):
                self.stare = "S0"
                return "S0", 0
            elif (a, b) == (1, 1):
                return "S1", 1

class Moore:
    def __init__(self):
        self.stare = "S0"
        self.iesiri = {"S0": 0, "S1": 1}

    def tranzitie(self, a, b):
        if self.stare == "S0":
            if (a, b) in [(0, 0), (1, 0)]:
                self.stare = "S0"
            else:
                self.stare = "S1"
        elif self.stare == "S1":
            if (a, b) == (1, 0):
                self.stare = "S0"
            else:
                self.stare = "S1"
        return self.stare, self.iesiri[self.stare]
 
m = Mealy()
mr = Moore()
semnale = [(0,0), (0,1), (1,0), (1,1), (0,0), (0,1), (1,0), (1,1)]
print("Mealy:")
for s in semnale:
    print(m.tranzitie(*s))
print("Moore:")
for s in semnale:
    print(mr.tranzitie(*s))
