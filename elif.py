#!/usr/bin/env python3

# if, elif and else logic statement showing soccer teams and their respective leagues

laLiga = ["Barcelona", "Real Madrid", "Athletico Madrid", "Getafe"]

EPL = ["Man City", "Man United", "Arsenal", "PSG"]

French_league = ["PSG", "Lille", "Marseille"]

if "Getafe" in EPL:
    print("I love this game")
    print("Yay!")

elif "Getafe" and "Barcelona" in laLiga:
    print("Yass! you nailed it")
elif "PSG" in EPL and "PSG" in French_league:
    print("Let's roll")
else:
    print("Try again")
