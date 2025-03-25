from typing import List, Dict, Tuple

class Bloemenwinkel:
    def __init__(self):
        # Initialiseer de voorraad en prijzen voor verschillende bloemen.
        self.voorraad: Dict[str, int] = {"roos": 100, "tulpen": 80, "zonnebloem": 50, "orchidee": 30}
        self.prijzen: Dict[str, float] = {"roos": 2.5, "tulpen": 1.8, "zonnebloem": 3.0, "orchidee": 5.0}
        self.bestellingen: List[Tuple[str, str, int, float]] = []

    def toon_voorraad(self) -> None:
        """Print de huidige voorraad van alle bloemen."""
        for bloem, aantal in self.voorraad.items():
            print(f"{bloem}: {aantal} stuks beschikbaar")

    def plaats_bestelling(self, klant_naam: str, bloem: str, aantal: int) -> None:
        """Plaats een bestelling voor een klant."""
        if bloem not in self.voorraad or aantal > self.voorraad[bloem]:
            print(f"Sorry, niet genoeg {bloem} op voorraad." if bloem in self.voorraad else f"Sorry, {bloem} is niet beschikbaar.")
            return

        prijs = self.prijzen[bloem] * aantal

        # Korting van 10% als het aantal bloemen meer dan of gelijk aan 10 is.
        if aantal >= 10:
            prijs -= prijs * 0.1
            print(f"Ge hebt 10% korting gekregen! Nieuwe prijs: {prijs:.2f} EUR")

        # Voeg de bestelling toe aan de lijst en verminder de voorraad.
        self.bestellingen.append((klant_naam, bloem, aantal, prijs))
        self.voorraad[bloem] -= aantal
        print(f"Uw bestelling is geplaatst voor {klant_naam}: {aantal} {bloem}(en). Totaal: {prijs:.2f} EUR")

    def toon_bestellingen(self) -> None:
        """Toon alle geplaatste bestellingen."""
        for naam, bloem, aantal, prijs in self.bestellingen:
            print(f"{naam} bestelde {aantal} {bloem}(en) voor {prijs:.2f} EUR")

# Voorbeeldgebruik van de Bloemenwinkel
winkel = Bloemenwinkel()
winkel.toon_voorraad()
winkel.plaats_bestelling("Jan", "roos", 12)
winkel.plaats_bestelling("Piet", "tulpen", 5)
winkel.plaats_bestelling("Karel", "orchidee", 2)
winkel.toon_bestellingen()
winkel.toon_voorraad()