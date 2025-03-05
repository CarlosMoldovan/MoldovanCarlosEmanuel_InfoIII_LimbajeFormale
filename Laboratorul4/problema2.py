class Masina:
    def __init__(self):
        self.stare = "S1"
        self.iesiri = {"S1": "O1", "S2": "O2"}
        self.tranzitii = {
            ("S1", "A"): "S1",
            ("S1", "B"): "S2",
            ("S2", "A"): "S1",
            ("S2", "B"): "S2"
        }
    
    def proces(self, intrari):
        for intrare in intrari:
            self.stare = self.tranzitii.get((self.stare, intrare), self.stare)
            print(f"Intrare: {intrare}, Stare: {self.stare}, Ieșire: {self.iesiri[self.stare]}")

masina = Masina()
intrari = input("Introduceți secvența de intrări (A/B, fără spații): ")
masina.proces(intrari)