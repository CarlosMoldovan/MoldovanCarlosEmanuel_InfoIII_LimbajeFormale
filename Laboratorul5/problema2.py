class NFA:
    def __init__(self, stari, alfa, tranz, start, fin):
        self.stari = stari
        self.alfa = alfa
        self.tranz = tranz
        self.start = start
        self.fin = fin

    def afis(self):
        print("Stari:", self.stari)
        print("Alfabet:", self.alfa)
        print("Tranzitii:")
        for k, v in self.tranz.items():
            print(k, "->", v)
        print("Start:", self.start)
        print("Finale:", self.fin)

stari = {"q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8"}
alfa = {"a", "b"}
tranz = {
    ("q0", ""): {"q1", "q4"},
    ("q1", "b"): {"q2"},
    ("q2", "a"): {"q3"},
    ("q2", "b"): {"q3"},
    ("q3", ""): {"q6"},
    ("q4", "a"): {"q5"},
    ("q5", ""): {"q6"},
    ("q6", "a"): {"q7"},
    ("q6", "b"): {"q7"},
    ("q7", ""): {"q8"},
}
start = "q0"
fin = {"q8"}
nfa = NFA(stari, alfa, tranz, start, fin)
nfa.afis()
