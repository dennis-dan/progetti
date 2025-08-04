import json
import os
from tipi_ingredienti import tipi_ingredienti

class Magazzino:
    """
    Gestione scorte ingredienti cocktail con aggiornamento file JSON.
    Struttura scorte:
    {ingrediente: [num_bottiglie, cl_rimanenti_in_bottiglia, tipo_alcol_o_allungante]}
    """

    def __init__(self, percorso_file_scorte: str = "dati/scorte.json"):
        self.percorso_file_scorte = percorso_file_scorte
        self.scorte = self.carica_scorte()

    def carica_scorte(self):
        if not os.path.exists(self.percorso_file_scorte):
            self.scorte = {}
            self.salva_scorte()
        else:
            with open(self.percorso_file_scorte, "r") as f:
                self.scorte = json.load(f)
        return self.scorte

    def salva_scorte(self):
        with open(self.percorso_file_scorte, "w") as f:
            json.dump(self.scorte, f, indent=4)

    def verifica_scorte(self, drink):
        """
        Verifica se ci sono scorte sufficienti per preparare il cocktail.
        """
        for ingrediente in drink.ingredienti:
            ingr = ingrediente.lower()
            if ingr not in self.scorte or self.scorte[ingr][0] == 0:
                return False
        return True

    def scala_ingredienti(self, drink):
        """
        Scala le dosi di ogni ingrediente consumato per il cocktail.
        Ritorna False se scorte insufficienti.
        """
        for ingrediente in drink.ingredienti:
            ingr = ingrediente.lower()
            if ingr not in self.scorte:
                return False

            bottiglie, cl_rimanenti, tipo = self.scorte[ingr]
            quantita = drink.ingredienti[ingrediente]

            if cl_rimanenti < quantita:
                margine = quantita - cl_rimanenti
                bottiglie -= 1
                if bottiglie <= 0:
                    return False
                cl_rimanenti = 70 if tipo == 'alcol' else 100
                cl_rimanenti -= margine
            else:
                cl_rimanenti -= quantita

            self.scorte[ingr] = [bottiglie, cl_rimanenti, tipo]

        self.salva_scorte()
        return True

    def rifornisci(self, ingrediente: str, bottiglie: int = 1):
        """
        Aggiunge bottiglie al magazzino, usando il tipo da tipi_ingredienti.py
        Se ingrediente nuovo, inizializza con capacità corretta.
        """
        ingr = ingrediente.lower()
        tipo = tipi_ingredienti.get(ingr, "allungante")  # default a allungante se sconosciuto
        capacita = 70 if tipo == 'alcol' else 100

        if ingr in self.scorte:
            self.scorte[ingr][0] += bottiglie
        else:
            self.scorte[ingr] = [bottiglie, capacita, tipo]

        self.salva_scorte()
