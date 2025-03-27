def controleer_bezoeker(attractienaam, lengte, leeftijd, ouders_mee):
    # Definitie van de minimum eisen per attractie
    attracties = {
        "SuperSplash": {"min_leeftijd": 16, "min_lengte": 120},
        "The Ride to Happiness": {"min_leeftijd": 14, "min_lengte": 160},
        "Bumballoon": {"min_leeftijd": 0, "min_lengte": 60}
    }

    # Controleer of de attractienaam geldig is
    if attractienaam not in attracties:
        print(f"Error: '{attractienaam}' is geen geldige attractienaam.")
        return

    # Controleer of lengte en leeftijd geldige waarden zijn (positieve getallen)
    if not isinstance(lengte, int) or lengte < 0:
        print("Error: Lengte moet een positief getal zijn.")
        return
    if not isinstance(leeftijd, int) or leeftijd < 0:
        print("Error: Leeftijd moet een positief getal zijn.")
        return

    # Haal de minimum eisen op voor de huidige attractie
    min_leeftijd = attracties[attractienaam]["min_leeftijd"]
    min_lengte = attracties[attractienaam]["min_lengte"]

    # Controleer of de bezoeker aan de lengteeisen voldoet
    if lengte < min_lengte:
        print(f"Je bent te kort om in {attractienaam} te gaan. Je moet minstens {min_lengte} cm groot zijn.")
        return

    # Als de ouders niet mee zijn, controleer dan ook de leeftijd
    if not ouders_mee and leeftijd < min_leeftijd:
        print(f"Je bent te jong om alleen in {attractienaam} te gaan. Je moet minstens {min_leeftijd} jaar oud zijn.")
        return

    # Als alle controles zijn doorstaan, mag de bezoeker in de attractie
    print(f"Welkom bij {attractienaam}! Veel plezier!")

# Testcases
controleer_bezoeker("SuperSplash", 110, 18, False)  # Te kort
controleer_bezoeker("The Ride to Happiness", 150, 13, True)  # Met ouders mag, ondanks leeftijd
controleer_bezoeker("Bumballoon", 70, 5, False)  # Mag, want voldoet aan lengteeis