def bepaal_basisboete(snelheidsoverschrijding):
    """
    Bepaalt de basisboete op basis van de snelheidsoverschrijding.

    :param snelheidsoverschrijding: Het aantal km/u waarmee de snelheid is overschreden.
    :return: De basisboete in euro's.
    """
    if 0 < snelheidsoverschrijding <= 10:
        return 100
    elif snelheidsoverschrijding <= 20:
        return 200
    elif snelheidsoverschrijding <= 40:
        return 400
    elif snelheidsoverschrijding > 40:
        return 800
    else:
        return 0


def bereken_boete(max_snelheid, gereden_snelheid, opdeciemen):
    """
    Bereken de totale boete op basis van de maximumsnelheid,
    de gereden snelheid en de opdecimentenfactor.

    :param max_snelheid: De toegestane maximumsnelheid in km/u.
    :param gereden_snelheid: De werkelijk gereden snelheid in km/u.
    :param opdeciemen: De factor waarmee de basisboete wordt vermenigvuldigd.
    :return: Een string met de snelheidsoverschrijding en de te betalen boete.
    """
    snelheidsoverschrijding = gereden_snelheid - max_snelheid

    if snelheidsoverschrijding <= 0:
        return "Geen boete, u reed binnen de limiet."

    basisboete = bepaal_basisboete(snelheidsoverschrijding)
    totaal_boete = basisboete * opdeciemen

    return f"Snelheidsoverschrijding: {snelheidsoverschrijding} km/u\nTe betalen boete: €{totaal_boete}"


# Het invoeren van de maximale snelheid, de gereden snelheid en de opdecimentenfactor.
max_snelheid = int(input("Wat is de maximumsnelheid (in km/u)? "))
gereden_snelheid = int(input("Wat is de door u gereden snelheid (in km/u)? "))
opdeciemen = int(input("Geef de factor voor de opdecimenten: "))

# Print het resultaat van de berekening van de boete.
print(bereken_boete(max_snelheid, gereden_snelheid, opdeciemen))