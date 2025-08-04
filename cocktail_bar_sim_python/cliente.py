from cocktail import Cocktail
from bar import Bar

class Cliente:
    def __init__(self,budget:float):
        self.budget=budget
        self.bar=Bar()

    def ordina_drink(self,drink:Cocktail):
        if self.budget>=self.bar.prezzi[drink.nome]:
            r=self.bar.ordinazione(drink)
            if r!='ordine non effettuato': self.paga(drink)
        else:
            return 'Non hai abbastanza soldi'
    
    def paga(self,drink:Cocktail):
        self.budget-=self.bar.prezzi[drink.nome]
    
    def cocktail_accessibili(self):
        return [nome for nome, prezzo in self.bar.prezzi.items() if prezzo <= self.budget]
