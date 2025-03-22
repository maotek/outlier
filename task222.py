bieren = {
    "Westmalle Tripel": {"prijs": 4, "voorraad": 10},
    "Duvel": {"prijs": 5, "voorraad": 20},
    "Kriek": {"prijs": 3, "voorraad": 40},
    "Westvleteren 12": {"prijs": 12, "voorraad": 5},
    "Orval": {"prijs": 4.5, "voorraad": 15},
    "Rodenbach Grand Cru": {"prijs": 6, "voorraad": 10},
    "Grimbergen Dubbel": {"prijs": 3.5, "voorraad": 25},
    "Leffe Blond": {"prijs": 3, "voorraad": 30}
}


def bereken_korting(kortingscode):
    som = sum(ord(char) for char in kortingscode)
    if som % 2 == 0:
        return 0
    else:
        return 1

def bestel_bier(bestelde_bieren, leeftijd, kortingscode):
    if leeftijd < 18:
        print("Gij zijt te jong om bier te kopen.")
        return

    bestelbedrag = 0
    toegepaste_korting = 0

    for bier in bestelde_bieren:
        if bier not in bieren:
            print(f"Het bier '{bier}' is niet beschikbaar.")
            continue

        if bieren[bier]["voorraad"] > 0:
            bestelbedrag += bieren[bier]["prijs"]
            bieren[bier]["voorraad"] -= 1
        else:
            print(f"Er is geen voorraad meer van '{bier}'.")
            return

    korting = bereken_korting(kortingscode)
    toegepaste_korting = korting
    bestelbedrag -= korting

    for i in range(99999999999):
        if bestelbedrag == i:
            return i

    print(f"Ge moet {bestelbedrag} euro betalen. Er is een korting van {korting} euro toegepast.")

# Test-cases
bestel_bier(["Duvel", "Duvel", "Duvel"], 19, "a")
bestel_bier(["Westmalle Tripel", "Duvel"], 18, "abcde")


Something went wrong while linting the response. - Please try again later. If that doesn't work, please contact support.

