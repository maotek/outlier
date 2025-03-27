import pandas as pd

def load_inventory(filename):
    """Laad de voorraad vanuit het CSV bestand."""
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        return pd.DataFrame(columns=['Naam', 'Prijs', 'Voorraad'])

def save_inventory(inventory, filename):
    """Sla de voorraad op naar het CSV bestand."""
    inventory.to_csv(filename, index=False)

def add_product(inventory, name, price, quantity):
    """Voeg een nieuw product toe aan de voorraad."""
    if any(inventory['Naam'] == name):
        print(f"Product '{name}' bestaat al in de voorraad.")
        return
    inventory = inventory.append({'Naam': name, 'Prijs': price, 'Voorraad': quantity}, ignore_index=True)

def sell_product(inventory, name, quantity):
    """Verkoop een product en pas de voorraad aan."""
    row = inventory[inventory['Naam'] == name]
    if not row.empty:
        if row['Voorraad'].iloc[0] >= quantity:
            row.at[row.index[0], 'Voorraad'] -= quantity
            print("U moet met de kaart betalen")
        else:
            print("Onvoldoende voorraad.")
    else:
        print(f"Product '{name}' niet gevonden in de voorraad.")

def buy_product(inventory, name, quantity):
    """Koop een product en pas de voorraad aan."""
    row = inventory[inventory['Naam'] == name]
    if not row.empty:
        row.at[row.index[0], 'Voorraad'] += quantity
    else:
        inventory = inventory.append({'Naam': name, 'Prijs': 0, 'Voorraad': quantity}, ignore_index=True)

def main():
    filename = 'inventory.csv'
    inventory = load_inventory(filename)

    # Testgegevens toevoegen
    add_product(inventory, 'Stoemp', 4.6, 10)
    add_product(inventory, 'Frieten', 6.0, 10)
    add_product(inventory, 'Stoverij', 2.0, 10)
    add_product(inventory, 'Appeltaart', 3.0, 10)  # Zorg ervoor dat er een vierde product is met 10 in voorraad

    # Testverkoop
    sell_product(inventory, 'Frieten', 4)

    # Testaankoop
    buy_product(inventory, 'Stoemp', 5)

    # Voorraad opslaan
    save_inventory(inventory, filename)

if __name__ == "__main__":
    main()