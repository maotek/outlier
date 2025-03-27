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
        # Zet de Bakkerij_Refactor op met een standaard voorraad en prijzen
        self.bakkerij = Bakkerij()

    def test_normale_bestelling(self):
        # Test een normale bestelling met voldoende voorraad en geen kortingen
        result = self.bakkerij.neem_bestelling_op(["Luikse Wafel", "Limburgse Vlaai"], "12345", False)
        self.assertEqual(result, "De totaalprijs van uw bestelling is 12.0 euro.")
        self.assertEqual(self.bakkerij.voorraad["Luikse Wafel"], 4)
        self.assertEqual(self.bakkerij.voorraad["Limburgse Vlaai"], 9)

    def test_korting_klantenkaart(self):
        # Test een bestelling met klantenkaart korting
        result = self.bakkerij.neem_bestelling_op(["Liers Vlaaike"], "23456", False)
        self.assertEqual(result, "De totaalprijs van uw bestelling is 7.0 euro.")

    def test_korting_student(self):
        # Test een bestelling met studentenkorting
        result = self.bakkerij.neem_bestelling_op(["Limburgse Vlaai"], "12345", True)
        self.assertEqual(result, "De totaalprijs van uw bestelling is 4.5 euro.")

    def test_korting_hoeveelheid(self):
        # Test een bestelling met hoeveelheidskorting
        result = self.bakkerij.neem_bestelling_op(["Luikse Wafel", "Limburgse Vlaai", "Liers Vlaaike", "Luikse Wafel", "Limburgse Vlaai"], "12345", False)
        self.assertEqual(result, "De totaalprijs van uw bestelling is 28.0 euro.")

    def test_onvoldoende_voorraad(self):
        # Test een bestelling met onvoldoende voorraad
        result = self.bakkerij.neem_bestelling_op(["Limburgse Vlaai", "Limburgse Vlaai", "Limburgse Vlaai", "Limburgse Vlaai", "Limburgse Vlaai", "Limburgse Vlaai"], "12345", False)
        self.assertEqual(result, "Uw bestelling kan niet verwerkt worden vanwege onvoldoende voorraad.")

    def test_onbekend_gebakje(self):
        # Test een bestelling met een onbekend gebakje
        result = self.bakkerij.neem_bestelling_op(["Brugse Zotte"], "12345", False)
        self.assertEqual(result, "Uw bestelling kan niet verwerkt worden vanwege onvoldoende voorraad.")

    def test_negatieve_hoeveelheid(self):
        # Test een bestelling met een negatieve hoeveelheid
        result = self.bakkerij.neem_bestelling_op(["Luikse Wafel"], "12345", False)
        self.assertEqual(result, "De totaalprijs van uw bestelling is 6.5 euro.")

    def test_geen_gebakjes(self):
        # Test een bestelling zonder gebakjes
        result = self.bakkerij.neem_bestelling_op([], "12345", False)
        self.assertEqual(result, "De totaalprijs van uw bestelling is 0.0 euro.")

    def test_meerdere_kortingen(self):
        # Test een bestelling met meerdere kortingen
        result = self.bakkerij.neem_bestelling_op(["Luikse Wafel", "Limburgse Vlaai", "Liers Vlaaike", "Luikse Wafel"], "23456", True)
        self.assertEqual(result, "De totaalprijs van uw bestelling is 24.0 euro.")

    def test_leeftijd_studentenkorting(self):
        # Test dat studentenkorting alleen geldt voor klanten jonger dan 26
        result = self.bakkerij.neem_bestelling_op(["Luikse Wafel"], "12345", True, 25)
        self.assertEqual(result, "De totaalprijs van uw bestelling is 6.5 euro.")
        result = self.bakkerij.neem_bestelling_op(["Luikse Wafel"], "12345", True, 26)
        self.assertEqual(result, "De totaalprijs van uw bestelling is 7.5 euro.")

if __name__ == '__main__':
    unittest.main()