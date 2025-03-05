class Masina:
    def __init__(self):
        self.stare = "Q1"
        self.tranzitii = {
            ("Q1", "X"): ("Q2", "O1"),
            ("Q1", "Y"): ("Q1", "O1"),
            ("Q2", "X"): ("Q1", "O2"),
            ("Q2", "Y"): ("Q2", "O2")
        }
    
    def proces(self, intrari):
        for intrare in intrari:
            if (self.stare, intrare) in self.tranzitii:
                self.stare, iesire = self.tranzitii[(self.stare, intrare)]
                print(f"Intrare: {intrare}, Stare: {self.stare}, Ieșire: {iesire}")
            else:
                print(f"Intrare invalidă: {intrare}")

masina = Masina()
intrari = input("Introduceți secvența de intrări (X/Y, fără spații): ")
masina.proces(intrari)
