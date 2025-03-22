class Bakkerij:
    def __init__(self):
        # Beginvoorraad van gebakjes
        self.voorraad = {
            "Luikse Wafel": 10,
            "Limburgse Vlaai": 10,
            "Liers Vlaaike": 10,
            "Antwerpse Handjes": 10,
            "Mattentaart": 10,
        }
        # Prijzen van gebakjes
        self.prijzen = {
            "Luikse Wafel": 5,
            "Limburgse Vlaai": 10,
            "Liers Vlaaike": 15,
            "Antwerpse Handjes": 10,
            "Mattentaart": 5,
        }

    def neem_bestelling_op(self, gebakjes, klantenkaartcode, is_student):
        totaal_prijs = 0
        bestelling_geldig = True

        # Check voorraad en bereken totaal prijs
        for gebak in gebakjes:
            if self.voorraad.get(gebak, 0) <= 0:
                print(f"Sorry, {gebak} is niet meer in voorraad.")
                bestelling_geldig = False
                break
            self.voorraad[gebak] -= 1
            totaal_prijs += self.prijzen[gebak]

        # Annuleer bestelling als ze niet geldig is
        if not bestelling_geldig:
            print("De bestelling kan niet verwerkt worden vanwege onvoldoende voorraad.")
            return

        # Kortingen toepassen
        korting = 0
        if int(klantenkaartcode) % 2 == 0:
            korting += 2
            print("U krijgt 2 euro korting dankzij uw klantenkaart.")
        if is_student:
            korting += 1
            print("U krijgt 1 euro korting als student.")
        if len(gebakjes) >= 5:
            korting += 3
            print("U krijgt 3 euro korting omdat u 5 of meer gebakjes bestelt.")

        totaal_prijs -= korting

        # Toon de totaalprijs
        print(f"De totaalprijs van uw bestelling is {totaal_prijs} euro.")


# Test de applicatie met drie verschillende bestellingen
bakkerij = Bakkerij()

print("\n--- Test 1 ---")
bakkerij.neem_bestelling_op(["Luikse Wafel", "Limburgse Vlaai"], "12345", True)

print("\n--- Test 2 ---")
bakkerij.neem_bestelling_op(["Mattentaart", "Mattentaart", "Mattentaart", "Mattentaart", "Mattentaart"], "24680", False)

print("\n--- Test 3 ---")
bakkerij.neem_bestelling_op(["Liers Vlaaike", "Antwerpse Handjes"], "13579", False)