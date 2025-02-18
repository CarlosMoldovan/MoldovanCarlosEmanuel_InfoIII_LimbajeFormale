class Start:
    def __init__(self):
        self.stari = {"q0", "q1", "q2", "q3"} 
        self.alf = {"a", "b", "c", "d"} 
        self.tranzitii = {
            "q0": {"a": "q1", "b": "q0", "c": "q0", "d": "q0"},
            "q1": {"a": "q1", "b": "q2", "c": "q1", "d": "q1"},
            "q2": {"a": "q2", "b": "q2", "c": "q2", "d": "q3"},
            "q3": {"a": "q3", "b": "q3", "c": "q3", "d": "q3"},
        }
        self.stari_i = "q0"
        self.stari_f = {"q3"}

    def proces(self, word):
        state = self.stari_i
        print(f"Stare initiala: {state}")
        for char in word:
            if char not in self.alf:
                print(f"Caracter invalid '{char}'! Cuvant respins.")
                return False 
            state = self.tranzitii[state].get(char, "q0")
            print(f"Caracter citit: '{char}', Stare actuala: {state}")
        is_accepted = state in self.stari_f
        print(f"Cuvant acceptat: {is_accepted}")
        return is_accepted
 
x = Start()

cuv = input("Introduceti un cuvant format din 'a', 'b', 'c', 'd': ")
x.proces(cuv)
