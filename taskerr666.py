class BusTicketsAutomaat:
    def __init__(self):
        # Beginnen met 100 kaartjes
        self.totaal_kaartjes = 100
        self.totale_omzet = 0

    def bereken_prijs(self, leeftijd, bestemming):
        # Bereken de basisprijs op basis van de leeftijd
        if leeftijd <= 3:
            basis_prijs = 0
        elif 4 <= leeftijd <= 18:
            basis_prijs = 15
        elif 19 <= leeftijd <= 50:
            basis_prijs = 30
        else:
            basis_prijs = 18

        # Voeg de bestemmingskost toe
        if bestemming == "Antwerpen":
            bestemming_prijs = 5
        elif bestemming == "Leuven":
            bestemming_prijs = 8
        elif bestemming == "Gent":
            bestemming_prijs = 2
        else:
            raise ValueError("Ongeldige bestemming.")  # Foutmelding voor een ongeldige bestemming

        return basis_prijs + bestemming_prijs

    def verkoop_kaartjes(self, leeftijden, bestemmingen, aantal_kaartjes):
        # Controleer of de inputs geldig zijn
        if not isinstance(aantal_kaartjes, int) or aantal_kaartjes <= 0:
            raise ValueError("Aantal kaartjes moet een positief geheel getal zijn.")

        if len(leeftijden) != aantal_kaartjes or len(bestemmingen) != aantal_kaartjes:
            raise ValueError("Het aantal leeftijden en bestemmingen moet overeenkomen met het aantal kaartjes.")

        if self.totaal_kaartjes < aantal_kaartjes:
            raise ValueError("Niet genoeg kaartjes op voorraad.")

        totale_prijs = 0
        for leeftijd, bestemming in zip(leeftijden, bestemmingen):
            totale_prijs += self.bereken_prijs(leeftijd, bestemming)

        # Trek het aantal verkochte kaartjes af van de totale voorraad
        self.totaal_kaartjes -= aantal_kaartjes
        # Verhoog de totale omzet
        self.totale_omzet += totale_prijs

        # Geef een waarschuwing als de kaartjes bijna op zijn
        if self.totaal_kaartjes <= 10:
            print(f"Waarschuwing: slechts {self.totaal_kaartjes} kaartjes over!")

        return totale_prijs

    def toon_totale_omzet(self):
        return self.totale_omzet


# Tests voor de BusTicketsAutomaat
automaat = BusTicketsAutomaat()

# Test 1
try:
    prijs1 = automaat.verkoop_kaartjes([2], ["Antwerpen"], 1)
    print(f"Test 1 - Totaal te betalen: €{prijs1}")
except ValueError as e:
    print(f"Test 1 - Fout: {e}")

# Test 2
try:
    prijs2 = automaat.verkoop_kaartjes([10, 50], ["Gent", "Gent"], 2)
    print(f"Test 2 - Totaal te betalen: €{prijs2}")
except ValueError as e:
    print(f"Test 2 - Fout: {e}")

# Toon de totale omzet tot nu toe
print(f"Totale omzet: €{automaat.toon_totale_omzet()}")