print("Kvitto-appen startar!")

belopp = float(input("Skriv in belopp: "))
moms = belopp * 0.25
totalt = belopp + moms

print(f"Belopp: {belopp} kr")
print(f"Moms: {moms} kr")
print(f"Totalt: {totalt} kr")