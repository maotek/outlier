def bereken_korting(aantal_onder_18, aantal_jarigen):
    """
    Bereken de totale korting voor de klanten.

    Parameters:
        aantal_onder_18 (int): Het aantal personen onder 18 jaar.
        aantal_jarigen (int): Het aantal jarigen.

    Returns:
        float: De totale korting in euro's.
    """
    if aantal_onder_18 < 0 or aantal_jarigen < 0:
        print("Het aantal personen onder de 18 of het aantal jarigen kan niet negatief zijn.")
        return 0

    korting = 0
    korting += aantal_onder_18 * 2  # 2 euro korting per persoon onder de 18
    korting += aantal_jarigen * 5  # 5 euro korting per jarige
    return korting


def bereken_bedrag(gerechten, aantal_personen, aantal_onder_18, aantal_jarigen):
    """
    Bereken het totale bedrag van de bestelling met korting.

    Parameters:
        gerechten (list): Een lijst met gerechten die besteld zijn.
        aantal_personen (int): Het aantal personen dat eet.
        aantal_onder_18 (int): Het aantal personen onder 18 jaar.
        aantal_jarigen (int): Het aantal jarigen.

    Returns:
        float: Het totale te betalen bedrag in euro's.
    """
    prijzen = {
        "Stoofvlees met frieten": 10,
        "Paling in 't groen": 15,
        "Waterzooi": 20,
        "Tomaat-garnaal": 10
    }

    totale_bedrag = 0

    for gerecht in gerechten:
        if gerecht in prijzen:
            totale_bedrag += prijzen[gerecht]
        else:
            print(f"Beste klant, het gerecht '{gerecht}' moet apart afgerekend worden.")

    korting = bereken_korting(aantal_onder_18, aantal_jarigen)
    totale_bedrag -= korting  # Pas korting toe

    return totale_bedrag


# Testcases
testcases = [
    (["Stoofvlees met frieten", "Waterzooi"], 4, 2, 0),  # Verwachte output: 26
    (["Stoofvlees met frieten", "Waterzooi"], 4, 2, 1),  # Verwachte output: 21
    (["Tomaat-garnaal", "Tomaat-garnaal", "Paling in 't groen"], 3, 0, 2)  # Verwachte output: 25
]

for gerecht, aantal_personen, aantal_onder_18, aantal_jarigen in testcases:
    resultaat = bereken_bedrag(gerecht, aantal_personen, aantal_onder_18, aantal_jarigen)
    print(
        f"Resultaat voor {gerecht} met {aantal_personen} personen, {aantal_onder_18} onder de 18 jaar en {aantal_jarigen} jarige(n): {resultaat} euro")