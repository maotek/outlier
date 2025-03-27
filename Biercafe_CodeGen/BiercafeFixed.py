# Initialiseer de voorraad en prijzen van de bieren
bieren = {
    "Westmalle Tripel": {"prijs": 4, "voorraad": 10},
    "Duvel": {"prijs": 5, "voorraad": 20},
    "Kriek": {"prijs": 3, "voorraad": 40}
}

def bereken_korting(kortingscode):
    # Bereken de korting door de som van de karaktercodes modulo 2 te nemen
    som = sum(ord(char) for char in kortingscode)
    return som % 2

def bestel_bier(bestelde_bieren, leeftijd, kortingscode):
    # Controleer of de klant oud genoeg is
    if leeftijd < 18:
        print("Ge zijt te jong om bier te kopen.")
        return

    bestelbedrag = 0
    toegepaste_korting = 0

    for bier in bestelde_bieren:
        # Controleer of het bier bestaat in de voorraad
        if bier not in bieren:
            print(f"Het bier '{bier}' is niet beschikbaar.")
            continue

        # Controleer of er voldoende voorraad is
        if bieren[bier]["voorraad"] > 0:
            bestelbedrag += bieren[bier]["prijs"]
            bieren[bier]["voorraad"] -= 1
        else:
            print(f"Er is geen voorraad meer van '{bier}'.")

    # Bereken de korting en pas deze toe
    korting = bereken_korting(kortingscode)
    bestelbedrag -= korting

    # Print het totale bedrag dat de klant moet betalen
    print(f"Ge moet {bestelbedrag} euro betalen. Er is een korting van {korting} euro toegepast.")

# Test-cases
bestel_bier(["Duvel", "Duvel", "Duvel"], 19, "a")
bestel_bier(["Westmalle Tripel", "Duvel"], 18, "abcde")