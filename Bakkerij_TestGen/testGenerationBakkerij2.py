class Bakkerij:
    def __init__(self):
        # Voorraad en prijzen van verschillende gebakjes
        self.voorraad = {
            "Luikse Wafel": 5,
            "Limburgse Vlaai": 10,
            "Liers Vlaaike": 15,
        }

        self.prijzen = {
            "Luikse Wafel": 6.5,
            "Limburgse Vlaai": 5.5,
            "Liers Vlaaike": 10,
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
                return "Uw bestelling kan niet verwerkt worden vanwege onvoldoende voorraad."

            self.voorraad[gebak] -= 1
            totaal_prijs += self.prijzen[gebak]

        # Bereken kortingen
        korting = self.bereken_korting(klantenkaartcode, is_student, gebakjes)
        totaal_prijs -= korting

        return f"De totaalprijs van uw bestelling is {totaal_prijs} euro."

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
            print("Ge ontvangt 2 extra euro korting dankzij uw klantenkaart.")

        # Studentenkorting
        if is_student:
            korting += 1
            print("Ge ontvangt 1 euro korting als student.")

        # Hoeveelheidskorting
        if len(gebakjes) >= 5:
            korting += 3
            print("Ge ontvangt 3 euro korting omdat u 5 of meer gebakjes bestelt.")

        return korting


import unittest

class TestBakkerij(unittest.TestCase):
    def setUp(self):
        # Maak een nieuw Bakkerij object voor elke test
        self.bakkerij = Bakkerij()

    def test_normale_bestelling(self):
        # Test een normale bestelling zonder kortingen
        result = self.bakkerij.neem_bestelling_op(["Luikse Wafel", "Limburgse Vlaai"], "12345", False)
        self.assertEqual(result, "De totaalprijs van uw bestelling is 12.0 euro.")
        self.assertEqual(self.bakkerij.voorraad["Luikse Wafel"], 4)
        self.assertEqual(self.bakkerij.voorraad["Limburgse Vlaai"], 9)

    def test_bestelling_met_klantenkaartkorting(self):
        # Test een bestelling met klantenkaartkorting
        result = self.bakkerij.neem_bestelling_op(["Liers Vlaaike"], "23456", False)
        self.assertEqual(result, "De totaalprijs van uw bestelling is 7.0 euro.")
        self.assertEqual(self.bakkerij.voorraad["Liers Vlaaike"], 14)
        # self.assertIn("Ge ontvangt 2 extra euro korting dankzij uw klantenkaart.", result)

    def test_bestelling_met_studentenkorting(self):
        # Test een bestelling met studentenkorting
        result = self.bakkerij.neem_bestelling_op(["Limburgse Vlaai"], "34567", True)
        self.assertEqual(result, "De totaalprijs van uw bestelling is 4.5 euro.")
        self.assertEqual(self.bakkerij.voorraad["Limburgse Vlaai"], 9)
        # self.assertIn("Ge ontvangt 1 euro korting als student.", result)

    def test_bestelling_met_hoeveelheidskorting(self):
        # Test een bestelling met hoeveelheidskorting
        result = self.bakkerij.neem_bestelling_op(
            ["Luikse Wafel", "Luikse Wafel", "Luikse Wafel", "Limburgse Vlaai", "Limburgse Vlaai"],
            "45678", False
        )
        self.assertEqual(result, "De totaalprijs van uw bestelling is 26.0 euro.")
        self.assertEqual(self.bakkerij.voorraad["Luikse Wafel"], 2)
        self.assertEqual(self.bakkerij.voorraad["Limburgse Vlaai"], 8)
        # self.assertIn("Ge ontvangt 3 euro korting omdat u 5 of meer gebakjes bestelt.", result)

    def test_bestelling_met_alle_kortingen(self):
        # Test een bestelling met alle mogelijke kortingen
        result = self.bakkerij.neem_bestelling_op(
            ["Liers Vlaaike", "Liers Vlaaike", "Liers Vlaaike", "Luikse Wafel", "Limburgse Vlaai"],
            "56789", True
        )
        self.assertEqual(result, "De totaalprijs van uw bestelling is 38.0 euro.")
        self.assertEqual(self.bakkerij.voorraad["Liers Vlaaike"], 12)
        self.assertEqual(self.bakkerij.voorraad["Luikse Wafel"], 4)
        self.assertEqual(self.bakkerij.voorraad["Limburgse Vlaai"], 9)
        # self.assertIn("Ge ontvangt 2 extra euro korting dankzij uw klantenkaart.", result)
        # self.assertIn("Ge ontvangt 1 euro korting als student.", result)
        # self.assertIn("Ge ontvangt 3 euro korting omdat u 5 of meer gebakjes bestelt.", result)

    def test_onvoldoende_voorraad(self):
        # Test een bestelling met onvoldoende voorraad
        result = self.bakkerij.neem_bestelling_op(["Luikse Wafel", "Luikse Wafel", "Luikse Wafel", "Luikse Wafel", "Luikse Wafel"], "67890", False)
        self.assertEqual(result, "Uw bestelling kan niet verwerkt worden vanwege onvoldoende voorraad.")
        self.assertEqual(self.bakkerij.voorraad["Luikse Wafel"], 5)

    def test_onbestaand_gebakje(self):
        # Test een bestelling met een gebakje dat niet bestaat
        result = self.bakkerij.neem_bestelling_op(["Brugse Zot"], "78901", False)
        self.assertEqual(result, "Uw bestelling kan niet verwerkt worden vanwege onvoldoende voorraad.")

if __name__ == '__main__':
    unittest.main()