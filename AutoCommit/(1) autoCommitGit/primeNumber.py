def ist_primzahl(zahl):
    if zahl < 2:
        return False
    for i in range(2, int(zahl**0.5) + 1):
        if zahl % i == 0:
            return False
    return True

def primzahlen_bis_n(n):
    primzahlen = [i for i in range(2, n + 1) if ist_primzahl(i)]
    return primzahlen

# Beispiel: Primzahlen bis 50
n = 50
ergebnis = primzahlen_bis_n(n)
print(f"Primzahlen bis {n}: {ergebnis}")
