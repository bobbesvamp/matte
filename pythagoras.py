
from cmath import sqrt


def hypotenus(katet1, katet2):
    return sqrt( katet1**2 + katet2**2 )

def katet(hypo, katet1):
    return sqrt( hypo**2 - katet1**2 )

print("Velkommen til Eriks pythagoras program")
svar = input("Vil du finne katet eller hypotenus? (K/H)")

if svar == "H" or svar == "h": 
    a = float( input("Oppgi lengden på katet 1:") )
    print(f"Du skrev {a}")
    b = float( input("Oppgi lengden på katet 2:") )
    print(f"Du skrev {b}")
    c =hypotenus(a, b)
    print(f"Lengden av hypotenusen er {c:.3f}")
else:
    a = float( input("Oppgi lengden på katet:") )
    print(f"Du skrev {a}")
    b = float( input("Oppgi lengden på hypotenus:") )
    print(f"Du skrev {b}")
    c = katet(b, a)
    print(f"Lengden av den andre kateten er {c:.3f}")
