class Start:
    def __init__(self):
        self.stari = {"q0", "q1", "q2", "q3"}
        self.stari_i = "q0"
        self.stari_f = {"q3"}
        self.tranzitii = {
            "q0": { (0,0): "q3", (0,1): "q0", (1,0): "q1", (1,1): "q3" },
            "q1": { (0,0): "q3", (0,1): "q0", (1,0): "q1", (1,1): "q2" },
            "q2": { (0,0): "q3", (0,1): "q0", (1,0): "q3", (1,1): "q3" },
            "q3": { (0,0): "q3", (0,1): "q3", (1,0): "q3", (1,1): "q3" }
        }
    
    def proces_input(self, input_pairs):
        state = self.stari_i
        for pair in input_pairs:
            if pair in self.tranzitii[state]:
                state = self.tranzitii[state][pair]
            else:
                return "Eroare: intrare invalidă!"
        return state
 
x = Start()
input_s = []
while True:
    try:
        x, y = map(int, input("Introduceți două valori (0 sau 1), separate prin spațiu: ").split())
        if x not in {0, 1} or y not in {0, 1}:
            print("Eroare: valorile trebuie să fie 0 sau 1!")
            continue
        input_s.append((x, y))
    except ValueError:
        print("Eroare: introduceți doar numere valide!")
        continue
    
    cont = input("Doriți să continuați? (da/nu): ").strip().lower()
    if cont != "da":
        break

target_stari = x.proces_input(input_s)
print("Starea finală:", target_stari)