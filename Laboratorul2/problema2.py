import string

class Start:
    def __init__(self, cuv):
        self.alphabet = set(string.ascii_lowercase) 
        self.cuv = cuv
        self.stari = [f"q{i}" for i in range(len(cuv) + 1)]
        self.stari_i = "q0"
        self.stari_f = f"q{len(cuv)}"
        self.tranzitii = self.build()
    
    def build(self):
        transitions = {}
        for i, char in enumerate(self.cuv):
            transitions[f"q{i}"] = {char: f"q{i+1}"}
            for letter in self.alphabet:
                if letter != char:
                    transitions[f"q{i}"][letter] = "q0"
        transitions[self.stari_f] = {}
        return transitions
    
    def p_text(self, text):
        state = self.stari_i
        for char in text:
            print(f"Caracter citit: '{char}', Stare actuală: {state}") 
            if char in self.tranzitii[state]:
                state = self.tranzitii[state][char]
            else:
                state = "q0" 
            
            if state == self.stari_f:
                print(f"Stare finală atinsă: {state}")
                return True 
        print(f"Stare finală neatingă, ultima stare: {state}")
        return False
 
cuv = input("Introduceți cuvântul de căutat: ").strip().lower()
x = Start(cuv)
 
test = input("Introduceți textul: ").strip().lower()
if x.p_text(test):
    print(f"Cuvântul '{cuv}' a fost găsit!")
else:
    print(f"Cuvântul '{cuv}' NU a fost găsit!")
