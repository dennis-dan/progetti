#funzioni di supporto (input utente, validazioni, ecc...)

def scegli_numero_giocatori():
    while True:
        try:
            n=int(input('Scegli il numero di giocatori che partecipano alla sfida: '))
            if n>1: return n
        except ValueError:
            pass
        print('Valore non ammesso, digita un numero intero > 1')

def scegli_giocatori(n):
    lista_giocatori=[]
    for i in range(n):
        giocatore=input(f'Nome giocatore {i+1}: ' )
        lista_giocatori.append(giocatore)
    return lista_giocatori

# print(scegli_giocatori(scegli_numero_giocatori()))
