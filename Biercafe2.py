# Voorraad bieren met prijs en aantal beschikbaar
bieren = {
    "Westmalle Tripel": {"prijs": 4, "voorraad": 10},
    "Duvel": {"prijs": 5, "voorraad": 20},
    "Kriek": {"prijs": 3, "voorraad": 40}
}


def bestel_bier(gewenste_bieren, leeftijd, kortingscode):
    # Totaal bedrag zonder korting
    totaal_bedrag = 0

    # Controleer of de klant minstens 18 is
    if leeftijd < 18:
        print("Je bent te jong om alcohol te kopen.")
        return

    # Bereken de korting
    korting = bereken_korting(kortingscode)

    for bier in gewenste_bieren:
        if bier in bieren:
            if bieren[bier]["voorraad"] > 0:
                # Voeg het bier toe aan de bestelling en verminder de voorraad
                totaal_bedrag += bieren[bier]["prijs"]
                bieren[bier]["voorraad"] -= 1
            else:
                print(f"Helaas, {bier} is op voorraad.")
        else:
            print(f"Helaas, {bier} is niet beschikbaar.")

    # Als het totaal bedrag groter is dan 0, betekent dit dat er een succesvolle bestelling is geweest
    if totaal_bedrag > 0:
        te_betalen = totaal_bedrag - korting
        print(f"Je moet {te_betalen} euro betalen. (Korting: {korting} euro)")


def bereken_korting(kortingscode):
    # Bereken de korting door de som van de ASCII waarden te nemen modulo 2
    return sum(ord(char) for char in kortingscode) % 2


# Test-cases
bestel_bier(["Duvel", "Duvel", "Duvel"], 19, "a")  # Moet 10 euro betalen (5+5) met 0 korting
bestel_bier(["Westmalle Tripel", "Duvel"], 18, "abcde")  # Moet 9 euro betalen (4+5) met 1 korting
bestel_bier(["Kriek", "Kriek", "Kriek", "Kriek"], 17, "xyz")  # Moet afwijzen omdat de klant te jong is
bestel_bier(["Non-bestaand bier"], 20, "123")  # Moet melding geven dat het bier niet beschikbaar is
bestel_bier(["Duvel"], 19, "")  # Moet 5 euro betalen met 0 korting (lege kortingscode)