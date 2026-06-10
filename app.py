class Kvitto:
    def __init__(self, benamning, belopp):
        self.benamning = benamning
        self.belopp = belopp
        self.moms = belopp * 0.25
        self.totalt = belopp + self.moms

    def visa(self):
        print(f"{self.benamning}: {self.belopp} kr + moms = {self.totalt} kr")


# Här börjar programmet
kvitton = []

print("Kvitto-appen startar!")

while True:
    benamning = input("Vad gäller kvittot? (eller 'klar' för att avsluta): ")
    
    if benamning == "klar":
        break
    
    belopp = float(input("Skriv in belopp: "))
    
    kvitto = Kvitto(benamning, belopp)
    kvitton.append(kvitto)
    
    print(f"✓ Sparat!\n")

print("\n--- Sammanfattning ---")
for k in kvitton:
    k.visa()

total = sum(k.totalt for k in kvitton)
print(f"\nTotalt att bokföra: {total} kr")