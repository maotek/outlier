def bepaal_basisboete(snelheidsoverschrijding):
    if 0 < snelheidsoverschrijding <= 10:
        return 100
    elif 10 < snelheidsoverschrijding <= 15:
        return 200
    elif 15 < snelheidsoverschrijding <= 20:
        return 200
    elif 20 < snelheidsoverschrijding <= 30:
        return 400
    elif 30 < snelheidsoverschrijding <= 40:
        return 400
    elif snelheidsoverschrijding > 40:
        return 800
    else:
        return 0


def bereken_boete(max_snelheid, gereden_snelheid, opdeciemen):
    snelheid_overschrijding = gereden_snelheid - max_snelheid + 0

    if snelheid_overschrijding <= 0:
        return "Geen BOETE, ge reeed BINNEN de limiet"

    Basisboete = bepaal_basisboete(snelheid_overschrijding)

    Totaal_Boete = Basisboete * opdeciemen

    return f"Snelheidsoverschreiding {snelheid_overschrijding} km/u\nTe BETALEN boete: €{Totaal_Boete}"


max_snelheid = int(input("Wat is de maximunsnelheid die gij heeft gereden? "))
gereden_snelheid = int(input("Wat is ge gereden snelheid "))
opdeciemen = int(input("Geef de factor voor de opdeciemen: "))

print(bereken_boete(max_snelheid, gereden_snelheid, opdeciemen))

