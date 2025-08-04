from cliente import Cliente
from cocktail import Cocktail
from vendite import report_vendite
from bar import Bar
import random

def main():
    bar=Bar()
    bar.refresh_file_vendite()  #azzera il contenuto del file vendite.csv 
    print(bar.listino_prezzi())
    num_clienti = random.randint(3, 6)  # numero casuale di clienti
    for i in range(1, num_clienti + 1):
        budget = round(random.uniform(8, 20), 2)    #budget casuale non eccessivamente alto
        cliente = Cliente(budget)

        print(f"\n--- Cliente {i} (budget iniziale: €{budget:.2f}) ---")

        ordini_possibili = random.randint(1, 4)
        for _ in range(ordini_possibili):
            accessibili = cliente.cocktail_accessibili()
            if not accessibili:
                print(f"[Cliente {i}] Grazie, arrivederci.")
                break

            scelta = random.choice(accessibili)
            drink = Cocktail(scelta)
            print(f"[Cliente {i}] Ordina: {drink.nome.title()}")
            cliente.ordina_drink(drink)

    print("\n--- FINE GIORNATA ---")
    print(report_vendite())

if __name__ == "__main__":
    main()
