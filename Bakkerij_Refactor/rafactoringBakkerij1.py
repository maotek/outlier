class Bakkerij:
    def __init__(self):
        # Voorraad en prijzen van verschillende gebakjes
        self.voorraad = {
            "Luikse Wafel": 10,
            "Limburgse Vlaai": 10,
            "Liers Vlaaike": 10,
            "Antwerpse Handjes": 10,
            "Mattentaart": 10,
        }

        self.prijzen = {
            "Luikse Wafel": 5,
            "Limburgse Vlaai": 10,
            "Liers Vlaaike": 15,
            "Antwerpse Handjes": 10,
            "Mattentaart": 5,
        }

    def neem_bestelling_op(self, gebakjes, klantenkaartcode, is_student, leeftijd=18):
        """
        Verwerkt een bestelling van gebakjes, controleert op voorraad,
        berekent de totaalprijs en eventuele kortingen.

        Parameters:
            gebakjes (list): Lijst van gevraagde gebakjes.
            klantenkaartcode (str): Code van de klantenkaart.
            is_student (bool): Geeft aan of de klant een student is.
            leeftijd (int, optioneel): Leeftijd van de klant. Standaard is 18.
        """
        totaal_prijs = 0

        # Check voorraad en bereken totaalprijs
        for gebak in gebakjes:
            if self.voorraad.get(gebak, 0) <= 0:
                print(f"Sorry, {gebak} is niet meer in voorraad.")
                print("De bestelling kan niet verwerkt worden vanwege onvoldoende voorraad.")
                return

            self.voorraad[gebak] -= 1
            totaal_prijs += self.prijzen[gebak]

        # Bereken kortingen
        korting = self.bereken_korting(klantenkaartcode, is_student, gebakjes)
        totaal_prijs -= korting

        print(f"De totaalprijs van uw bestelling is {totaal_prijs} euro.")

    def bereken_korting(self, klantenkaartcode, is_student, gebakjes):
        """
        Berekent de totale korting voor de bestelling op basis van klantenkaart,
        studentenkorting en hoeveelheidskorting.

        Parameters:
            klantenkaartcode (str): Code van de klantenkaart.
            is_student (bool): Geeft aan of de klant een student is.
            gebakjes (list): Lijst van gevraagde gebakjes.

        Returns:
            int: Het totale kortingsbedrag.
        """
        korting = 0

        # Klantenkaart korting
        if int(klantenkaartcode) % 2 == 0:
            korting += 2
            print("U krijgt 2 euro korting dankzij uw klantenkaart.")

        # Studentenkorting
        if is_student:
            korting += 1
            print("U krijgt 1 euro korting als student.")

        # Hoeveelheidskorting
        if len(gebakjes) >= 5:
            korting += 3
            print("U krijgt 3 euro korting omdat u 5 of meer gebakjes bestelt.")

        return korting


# Voorbeeldgebruik van de Bakkerij klasse
bakkerij = Bakkerij()

print("\n--- Test 1 ---")
bakkerij.neem_bestelling_op(["Luikse Wafel", "Limburgse Vlaai"], "12345", True)

print("\n--- Test 2 ---")
bakkerij.neem_bestelling_op(["Mattentaart"] * 5, "24680", False)

print("\n--- Test 3 ---")
bakkerij.neem_bestelling_op(["Liers Vlaaike", "Antwerpse Handjes"], "13579", False)