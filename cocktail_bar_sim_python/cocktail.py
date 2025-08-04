import json
import os

class Cocktail:
    def __init__(self, nome: str, percorso_file_ricette: str = "dati/ricette.json", ingredienti: dict = {}):
        self.nome = nome.title()
        self.percorso_file_ricette = percorso_file_ricette
        
        if not os.path.exists(percorso_file_ricette):
            # Se il file non esiste, crealo vuoto
            with open(percorso_file_ricette, "w") as f:
                json.dump({}, f)
        
        with open(percorso_file_ricette, "r") as f:
            ricette = json.load(f)
        
        if self.nome in ricette:
            self.ingredienti = ricette[self.nome]
        else:
            if ingredienti:
                # Se ingredienti passati a init, usali e aggiorna il file
                self.ingredienti = ingredienti
                self._aggiorna_ricette_file()
            else:
                # Altrimenti chiedi all'utente di inserirli da console
                print(f"Ricetta per '{self.nome}' non trovata.")
                self.ingredienti = self._chiedi_ingredienti()
                self._aggiorna_ricette_file()

    def _chiedi_ingredienti(self):
        ingredienti = {}
        print("Inserisci ingredienti e dosi (in cl). Scrivi 'fine' per terminare.")
        while True:
            ingr = input("Ingrediente: ").strip().lower()
            if ingr == "fine":
                if ingredienti:
                    break
                else:
                    print("Devi inserire almeno un ingrediente.")
                    continue
            try:
                dose = float(input(f"Dose di {ingr} (cl): "))
                if dose <= 0:
                    print("Inserisci un numero positivo.")
                    continue
            except ValueError:
                print("Dose non valida, inserisci un numero.")
                continue
            ingredienti[ingr] = dose
        return ingredienti

    def _aggiorna_ricette_file(self):
        with open(self.percorso_file_ricette, "r") as f:
            ricette = json.load(f)
        ricette[self.nome] = self.ingredienti
        with open(self.percorso_file_ricette, "w") as f:
            json.dump(ricette, f, indent=4)
        print(f"Ricetta per '{self.nome}' aggiunta/aggiornata con successo.")

    
