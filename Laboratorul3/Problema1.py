class CoffeeMachineFSM:
    def __init__(self):
        self.states = {"q0": "Așteptare", "q1": "Cafea selectată", "q2": "Ceai selectat", 
                       "q3": "Cappuccino selectat", "q4": "Ciocolată caldă sau livrare finalizată"}
        self.state = "q0"
        
        self.transitions = {
            "q0": {"C": "q1", "T": "q2", "A": "q3", "H": "q4"},
            "q1": {"OK": "q4"},
            "q2": {"OK": "q4"},
            "q3": {"OK": "q4"},
            "q4": {"OK": "q0"}
        }
    
    def transition(self, action):
        if action in self.transitions.get(self.state, {}):
            self.state = self.transitions[self.state][action]
            print(f"Tranziție efectuată: {self.states[self.state]}")
        else:
            print("Acțiune invalidă. Încearcă din nou!")
    
    def run(self):
        print("Automat de băuturi - Alege o băutură: C (Cafea), T (Ceai), A (Cappuccino), H (Ciocolată caldă)")
        while True:
            action = input("Selectează o opțiune: ").strip().upper()
            if action == "EXIT":
                print("Oprire automat.")
                break
            self.transition(action)
 
automat = CoffeeMachineFSM()
automat.run()
