class ParkingLotFSM:
    def __init__(self, num_spots):
        self.num_spots = num_spots
        self.parking_spots = ["liber"] * num_spots 
    
    def show_parking_status(self):
        print("Starea parcării:")
        for i, status in enumerate(self.parking_spots, 1):
            print(f"Loc {i}: {status}")
    
    def park_car(self):
        if "liber" in self.parking_spots:
            index = self.parking_spots.index("liber")
            self.parking_spots[index] = "ocupat"
            print(f"Mașina a fost parcată la locul {index + 1}.")
        else:
            print("Parcarea este plină! Nu se poate parca.")
    
    def leave_parking(self, spot_number):
        if 1 <= spot_number <= self.num_spots and self.parking_spots[spot_number - 1] == "ocupat":
            self.parking_spots[spot_number - 1] = "liber"
            print(f"Mașina a plecat din locul {spot_number}.")
        else:
            print("Locul este deja liber sau numărul locului este invalid.")
    
    def run(self):
        print("Automat de parcare - Comenzi disponibile: PARK (parcare), LEAVE <număr loc>, STATUS, EXIT")
        while True:
            command = input("Introduceți comanda: ").strip().upper()
            if command == "EXIT":
                print("Oprire automat de parcare.")
                break
            elif command == "PARK":
                self.park_car()
            elif command.startswith("LEAVE"):
                parts = command.split()
                if len(parts) == 2 and parts[1].isdigit():
                    self.leave_parking(int(parts[1]))
                else:
                    print("Comandă invalidă. Folosiți LEAVE <număr loc>.")
            elif command == "STATUS":
                self.show_parking_status()
            else:
                print("Comandă invalidă. Încearcă din nou!")
 
automat_parcare = ParkingLotFSM(5)  
automat_parcare.run()
