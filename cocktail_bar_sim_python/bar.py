from magazzino import Magazzino
from cocktail import Cocktail
import json
import random
from tipi_ingredienti import tipi_ingredienti
import os
import random

class Bar:
    def __init__(self, percorso_file_ricette: str = "dati/ricette.json"):
        with open(percorso_file_ricette) as f:
            self.ricette = json.load(f)
        
        self.magazzino = Magazzino()
        self.prezzi = self.carica_o_genera_prezzi()
    
    def carica_o_genera_prezzi(self, percorso_file="dati/prezzi.json"):
        if os.path.isfile(percorso_file):
            with open(percorso_file, "r", encoding="utf-8") as f:
                prezzi = json.load(f)
            #print("✅ Prezzi caricati da file.")
        else:
            prezzi = self.genera_prezzi(self.ricette)
            with open(percorso_file, "w", encoding="utf-8") as f:
                json.dump(prezzi, f, indent=4)
            #print("🆕 Prezzi generati e salvati in 'dati/prezzi.json'.")
        return prezzi
    
    def genera_prezzi(self, ricette):  # carica o genera un file composto da un dizionario con nome_cocktail:costo_in_euro
        price = {}
        for cocktail in ricette:
            alcol = 0
            allungante = 0
            for ingrediente in ricette[cocktail]:
                tipo = tipi_ingredienti.get(ingrediente.lower(), "allungante")
                if tipo == 'alcol':
                    alcol += 1
                else:
                    allungante += 1
            base = alcol * 2 + allungante * 0.5
            extra = random.randint(1, 3) / 2.0
            price[cocktail] = round(base + extra, 1)
        return price

    def ordinazione(self, drink: Cocktail):
        if self.magazzino.verifica_scorte(drink):
            return self.prepara(drink)

        print(f"❌ Non ci sono scorte sufficienti per preparare {drink.nome}.")
        return self.richiedi_rifornimenti(drink)
    
    def richiedi_rifornimenti(self, drink: Cocktail):
        ingredienti = drink.ingredienti
        print(f"Ingredienti richiesti: {ingredienti}")
        print("🔄 Rifornimento automatico in corso...")

        for ingrediente in ingredienti:
            scorta = self.magazzino.scorte.get(ingrediente)
            if not scorta or scorta[0] == 0 or scorta[1]<ingredienti[ingrediente]:
                quantita = random.randint(1, 5)
                self.magazzino.rifornisci(ingrediente, quantita)
                print(f"➕ Rifornite {quantita} bottiglie di {ingrediente}.")
        return 'ordine non effettuato'


    #da chiamare nel main prima di registrare le vendite se si vuole lavorare su un file pulito
    def refresh_file_vendite(self, percorso_file_vendite='dati/vendite.csv'):   
        with open(percorso_file_vendite, mode='w') as f:
            f.write('')

    def prepara(self,drink):
        if self.magazzino.scala_ingredienti(drink):
            return self.ricevi_pagamento(drink)
        print(f"Non ci sono ingredienti sufficienti per preparare {drink.nome}")
        self.richiedi_rifornimenti(drink)

    def ricevi_pagamento(self, drink, percorso_file_vendite='dati/vendite.csv'):
        prezzo = self.prezzi.get(drink.nome, 0)
        nuova_riga = f"{drink.nome},{prezzo}"

        # Controlla se il file esiste e se contiene già dati
        aggiungi_newline = False
        try:
            with open(percorso_file_vendite, 'r', encoding='utf-8') as f:
                contenuto = f.read().strip()
                if contenuto:
                    aggiungi_newline = True
        except FileNotFoundError:
            pass  # Se non esiste, verrà creato

        with open(percorso_file_vendite, mode='a', encoding='utf-8') as f:
            if aggiungi_newline:
                f.write('\n' + nuova_riga)
            else:
                f.write(nuova_riga)

        print(f"{drink.nome} venduto a €{prezzo}.")

    def listino_prezzi(self):
        print('         MENU           ')
        print('| Nome cocktail | Prezzo |')
        print('-------------------------')
        for cocktail in self.prezzi:
                print(f'| {cocktail} | {self.prezzi[cocktail]}|')
        return '_____________________'

        
