import pandas as pd


class CapsuleAutomaat:
    def __init__(self):
        self.inhoud = pd.DataFrame(columns=['Speelgoed', 'Aantal'])

    def laad_inhoud(self, inhoud_data):
        nieuwe_inhoud = pd.DataFrame(inhoud_data, columns=['Speelgoed', 'Aantal'])
        self.inhoud = pd.concat([self.inhoud, nieuwe_inhoud]).groupby('Speelgoed', as_index=False).sum()
        print("Ge heeft de inhoud ingeladen!")

    def toon_inhoud(self):
        if self.inhoud.empty:
            print("De machine is leeg!")
        else:
            print("Huidige inhoud van de Capsule Machine:")
            print(self.inhoud)

    def trek_speelgoed(self):
        if self.inhoud.empty:
            print("De machine is leeg! Geen speelgoed om te trekken.")
            return None

        beschikbare_speelgoed = self.inhoud[self.inhoud['Aantal'] > 0]

        if beschikbare_speelgoed.empty:
            print("Er is geen speelgoed beschikbaar om te trekken.")
            return None

        getrokken_speelgoed = beschikbare_speelgoed.sample()
        speelgoed_naam = getrokken_speelgoed['Speelgoed'].values[0]

        # Verminder het aantal van het getrokken speelgoed met 1
        self.inhoud.loc[self.inhoud['Speelgoed'] == speelgoed_naam, 'Aantal'] -= 1

        print(f"Gefeliciteerd! Gij heeft een {speelgoed_naam} getrokken.")

        return speelgoed_naam


def test_capsule_automaat():
    automaat = CapsuleAutomaat()

    init_inhoud = [
        ('Cijferdobbelbak', 5),
        ('Pudebak', 3),
        ('Mini Pop', 4),
        ('Actiefiguur', 2)
    ]

    automaat.laad_inhoud(init_inhoud)

    automaat.toon_inhoud()

    automaat.trek_speelgoed()
    automaat.trek_speelgoed()
    automaat.trek_speelgoed()

    automaat.toon_inhoud()


test_capsule_automaat()