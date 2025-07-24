#lancio dadi e valuta combinazioni
import random
from collections import Counter

def lancia_dadi(n=5):
    dadi=[]
    for i in range(n):
        dado=random.randint(1,6)
        dadi.append(dado)
    print(f'La tua combinazione è: {dadi}')
    return dadi

def cambia_dadi(dadi):
    print('Scegli quali dadi vuoi rilanciare (uno alla volta seguiti da ENTER/INVIO), digita q per terminare.')
    while True:
        try:
            scelta=int(input())
            if scelta < 1 or scelta > 5: print('Dado inesistente, riprova') 
            else: dadi[scelta-1]=random.randint(1,6)
        except ValueError:
            break
    print(f'La tua combinazione finale è: {dadi}')
    return dadi

def valuta_combinazione(dadi):
    conta=Counter(dadi)
    chiavi=list(conta.keys())
    valori=list(conta.values())

    if sorted(dadi)==[1,2,3,4,5]: return 'scala', 5
    elif sorted(dadi)==[2,3,4,5,6]: return 'scala', 6
    else:
        if 5 in valori:
            val = chiavi[valori.index(5)]
            return 'yahtzee', val
        elif 4 in valori:
            val = chiavi[valori.index(4)]
            return 'poker', val
        elif 3 in valori and 2 in valori:
            val_tris = chiavi[valori.index(3)]
            return 'full', val_tris
        elif 3 in valori:
            val = chiavi[valori.index(3)]
            return 'tris', val
        elif valori.count(2)==2:
            values = [el for el in chiavi if conta[el]==2]
            return 'doppia coppia', max(values)
        elif 2 in valori:
            val = chiavi[valori.index(2)]
            return 'coppia', val
        else:
            return 'nulla', max(dadi)


#print(valuta_combinazione(cambia_dadi(lancia_dadi())))