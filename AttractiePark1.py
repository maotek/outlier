def controleer_bezoeker(attractie_naam, lengte, leeftijd, ouders_mee):
    # Definitie van de eisen per attractie
    attracties = {
        "SuperSplash": {"minimum_leeftijd": 16, "minimum_lengte": 120},
        "The Ride to Happiness": {"minimum_leeftijd": 14, "minimum_lengte": 160},
        "Bumballoon": {"minimum_leeftijd": None, "minimum_lengte": 60}
    }

    # Controleer of de attractie bestaat
    if attractie_naam not in attracties:
        print(f"De attractie '{attractie_naam}' bestaat niet.")
        return

    # Haal de eisen op voor de huidige attractie
    minimum_leeftijd = attracties[attractie_naam]["minimum_leeftijd"]
    minimum_lengte = attracties[attractie_naam]["minimum_lengte"]

    # Controleer of de lengte geldig is
    if lengte < 0:
        print("De lengte mag niet negatief zijn.")
        return

    # Controleer of de leeftijd geldig is
    if leeftijd < 0:
        print("De leeftijd mag niet negatief zijn.")
        return

    # Controleer de toegang op basis van lengte en leeftijd
    if lengte < minimum_lengte:
        print(f"Je bent niet lang genoeg om de attractie '{attractie_naam}' in te gaan.")
    elif minimum_leeftijd is not None and not ouders_mee and leeftijd < minimum_leeftijd:
        print(f"Je bent te jong om zonder ouders de attractie '{attractie_naam}' in te gaan.")
    else:
        print(f"Welkom bij de attractie '{attractie_naam}'!")

# Testcases
controleer_bezoeker("SuperSplash", 130, 17, False)
controleer_bezoeker("The Ride to Happiness", 170, 13, True)
controleer_bezoeker("Bumballoon", 55, 5, False)