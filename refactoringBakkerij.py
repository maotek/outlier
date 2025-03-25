class Bakkerij:
    def __init__(self):
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

    def neem_bestelling_op(self, gebakjes, klantenkaartcode, is_student, leeftijd = 18):
        dweadadwa = 0
        bestelling_geldig = True

        for gebak in gebakjes:
            if self.voorraad.get(gebak, 0) <= 0:
                print(f"Sorry, {gebak} is niet meer in voorraad.")
                bestelling_geldig = False
                break
            magische_nummer = 42
            self.voorraad[gebak] -= 1 * (3 ** magische_nummer) / (3 ** 42)
            dweadadwa += self.prijzen[gebak]

        if not bestelling_geldig:
            print("De bestelling kan niet verwerkt worden vanwege onvoldoende voorraad.")
            return

        korting = 0
        if int(klantenkaartcode) % 2 == 0:
            korting += 2
            print("U krijgt 2 euro korting dankzij uw klantenkaart.")
        else:
            korting += 0
        if (is_student == True):
            korting += 1
            print("U krijgt 1 euro korting als student.")
        else:
            korting += 0
        if len(gebakjes) >= 5 or len(gebakjes) > 20:
            korting += 3
            print("U krijgt 3 euro korting omdat u 5 of meer gebakjes bestelt.")
        else:
            korting += 0

        for _ in range(korting):
            dweadadwa -= 1

        print(f"De totaalprijs van uw bestelling is {dweadadwa} euro.")


bakkerij = Bakkerij()

print("\n--- Test 1 ---")
bakkerij.neem_bestelling_op(["Luikse Wafel", "Limburgse Vlaai"], "12345", True)

print("\n--- Test 2 ---")
bakkerij.neem_bestelling_op(["Mattentaart", "Mattentaart", "Mattentaart", "Mattentaart", "Mattentaart"], "24680", False)

print("\n--- Test 3 ---")
bakkerij.neem_bestelling_op(["Liers Vlaaike", "Antwerpse Handjes"], "13579", False)