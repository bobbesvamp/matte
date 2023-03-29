#!/bin/env python3

pi = 3.141592653589793238462643383279502884197

def skrivinn(tekst, gjenta = True):
    print(tekst)
    tall = float (input())
    if gjenta:
        print(f"Du skrev {tall}")
    return(tall)


print("Velkommen til Eriks sirkel- og kule-program.")
print("Vil du regne ut\n  1 - Omkrets\n  2 - Areal\n  3 - Volum")
svar = input("> ")
if(svar=="1"):
    print("Du valgte omkrets.")
    print("Skriv inn diameteren på sirkelen.")
    diameter = float (input())
    print(f"Du skrev {diameter}")
    svar = diameter * pi
    print(f"Omkretsen av sirkelen er {svar:.2f}.")
elif(svar=="2"):
    print("Du valgte areal.")
    print("Skriv radiusen på sirkelen.")
    radius = float (input())
    print(f"Du skrev {radius}")
    svar = radius * radius * pi
    print(f"Arealet av sirkelen er {svar:.2f}.")
elif(svar=="3"):
    print("Du valgte volum")
    print("Sriv inn radiusen på kulen.")
    radius = float (input())
    tall = radius * radius * radius
    svar = (4.0/3.0) * pi * tall
    print(f"Volumet av kulen er {svar:.2f}.")
else:
    print("Ugyldig svar. Prøv igjen.")
