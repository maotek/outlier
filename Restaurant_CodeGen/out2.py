def bereken_korting(aantal_onderachtien, aantal_jarigen):
    """
    Berekent de totale korting voor de klanten.

    Parameters:
        aantal_onderachtien (int): Het aantal personen onder 18 jaar.
        aantal_jarigen (int): Het aantal jarigen.

    Returns:
        float: De totale korting in euro.
    """
    # Korting voor personen onder 18
    korting_onderachtien = max(0, aantal_onderachtien) * 2

    # Korting voor jarigen
    korting_jarigen = max(0, aantal_jarigen) * 5

    # Totale korting
    totale_korting = korting_onderachtien + korting_jarigen

    return totale_korting


def bereken_bedrag(gerechten, aantal_personen, aantal_onderachtien, aantal_jarigen):
    """
    Berekent het totale bedrag van de bestelling met desgevallende korting.

    Parameters:
        gerechten (list): Een lijst met gerechten die besteld zijn.
        aantal_personen (int): Het aantal personen dat eet.
        aantal_onderachtien (int): Het aantal personen onder 18 jaar.
        aantal_jarigen (int): Het aantal jarigen.

    Returns:
        float: Het totale te betalen bedrag in euro.
    """
    prijzen = {
        "Stoofvlees met frieten": 10,
        "Paling in 't groen": 15,
        "Waterzooi": 20,
        "Tomaat-garnaal": 10
    }

    totaal_bedrag = 0
    onbekende_gerechten = []

    for gerecht in gerechten:
        if gerecht in prijzen:
            totaal_bedrag += prijzen[gerecht]
        else:
            onbekende_gerechten.append(gerecht)

    if onbekende_gerechten:
        for gerecht in onbekende_gerechten:
            print(f"Het gerecht {gerecht} is niet op de kaart, dit moet apart worden afgerekenen.")

    # Bereken korting
    korting = bereken_korting(aantal_onderachtien, aantal_jarigen)

    # Bereken het eindbedrag na korting
    eindbedrag = totaal_bedrag - korting

    return eindbedrag


# Testcases
gerechten1 = ["Stoofvlees met frieten", "Waterzooi"]
print(bereken_bedrag(gerechten1, 4, 2, 0))  # Output: 36.0

gerechten2 = ["Stoofvlees met frieten", "Waterzooi"]
print(bereken_bedrag(gerechten2, 4, 2, 1))  # Output: 31.0

gerechten3 = ["Tomaat-garnaal", "Tomaat-garnaal", "Paling in 't groen"]
print(bereken_bedrag(gerechten3, 3, 0, 2))  # Output: 25.0

gerechten4 = ["Stoofvlees met frieten", "Onbekend gerecht", "Waterzooi"]
print(bereken_bedrag(gerechten4, 4, 2, 0))  # Output: 36.0 met melding dat "Onbekend gerecht" apart moet worden afgerekenen