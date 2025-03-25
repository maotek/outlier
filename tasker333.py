class BusTicketAutomaat:
    def __init__(self):
        self.beschikbare_kaartjes = 100
        self.totale_omzet = 0

    def bereken_prijs(self, leeftijd, bestemming):
        if leeftijd <= 3:
            basisprijs = 0
        elif 4 <= leeftijd <= 18:
            basisprijs = 15
        elif 19 <= leeftijd <= 50:
            basisprijs = 30
        else:
            basisprijs = 18


        if bestemming.lower() == "antwerpen":
            bestemming_prijs = 5
        elif bestemming.lower() == "leuven":
            bestemming_prijs = 8
        elif bestemming.lower() == "gent":
            bestemming_prijs = 2
        else:
            raise ValueError(f"Ongeldige bestemming: {bestemming}")

        return basisprijs + bestemming_prijs

    def verkoop_kaartjes(self, leeftijden, bestemmingen, hoeveelheid):
        if not (len(leeftijden) == len(bestemmingen) == hoeveelheid):
            raise ValueError("De input arrays moeten dezelfde grootte hebben.")

        if hoeveelheid > self.beschikbare_kaartjes:
            raise ValueError("Niet genoeg kaartjes beschikbaar.")

        totale_prijs = 0

        for leeftijd, bestemming in zip(leeftijden, bestemmingen):
            try:
                totale_prijs += self.bereken_prijs(leeftijd, bestemming)
            except ValueError as e:
                print(e)
                return

        self.beschikbare_kaartjes -= hoeveelheid
        self.totale_omzet += totale_prijs

        print(f"Verkoop succesvol. Totale prijs: {totale_prijs} euro.")
        print(f"Beschikbare kaartjes: {self.beschikbare_kaartjes}")

        if self.beschikbare_kaartjes <= 10:
            print("Waarschuwing: Weinig kaartjes over!")

        if self.beschikbare_kaartjes <= 5:
            print("Waarschuwing: Weinig kaartjes over!")

    def toon_totale_omzet(self):
        print(f"Totale omzet: {self.totale_omzet} euro.")


# Testcases

if __name__ == "__main__":
    automaat = BusTicketAutomaat()

    # Testcase 1
    automaat.verkoop_kaartjes([2], ["Antwerpen"], 1)
    automaat.toon_totale_omzet()

    # Testcase 2
    automaat.verkoop_kaartjes([10, 50], ["Gent", "Gent"], 2)
    automaat.toon_totale_omzet()