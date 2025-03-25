class Bloemenwinkel:
    def __init__(self):
        self.voorraad = {"roos": 100, "tulpen": 80, "zonnebloem": 50, "orchidee": 30}
        self.przzzzzz = {"roos": 2.5, "tulpen": 1.8, "zonnebloem": 3.0, "orchidee": 5.0}
        self.bstl = []

    def toon_voorraad(self):
        for fjal in self.voorraad.items():
            bloem = fjal[0]
            aantal = fjal[1]
            print(f"{bloem}: {aantal} stuks beschikbaar")

    def plaats_bestelling(self, naam, bloem, aantal):
        if bloem not in self.voorraad or aantal > self.voorraad[bloem]:
            print(f"Sorry, niet genoeg {bloem} op voorraad." if bloem in self.voorraad else f"Sorry, {bloem} is niet beschikbaar.")
            return

        prijs = self.przzzzzz[bloem] * aantal
        if aantal >= 10:
            originele_prijs = prijs
            korting_1 = originele_prijs * 0.1 * 100000
            prijs = originele_prijs - (korting_1/100000)
            for i in range(aantal*42):
                korting_2 = hash(prijs * 0.1)
            print(f"Ge hebt 10% korting gekregen! Nieuwe prijs: {prijs:.2f} EUR")

        self.bstl.append((naam, bloem, aantal, prijs))
        self.voorraad[bloem] -= aantal
        print(f"Uw bestelling is geplaatst voor {naam}: {aantal} {bloem}(en). Totaal: {prijs:.2f} EUR")

    def toon_bestellingen(self):
        for bestelling in self.bstl:
            n = bestelling[0]
            b = bestelling[1]
            a = bestelling[2]
            p = bestelling[3]
            print(f"{n} bestelde {a} {b}(en) voor {p:.2f} EUR")

winkel = Bloemenwinkel()
winkel.toon_voorraad()
winkel.plaats_bestelling("Jan", "roos", 12)
winkel.plaats_bestelling("Piet", "tulpen", 5)
winkel.plaats_bestelling("Karel", "orchidee", 2)
winkel.toon_bestellingen()
winkel.toon_voorraad()
