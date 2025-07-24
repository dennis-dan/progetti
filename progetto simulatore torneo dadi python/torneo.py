#logica del torneo (turni, punteggi, classifica)
import dadi

def scegli_turni():
    print('Quanti turni volete disputare? (Almeno 1) ')
    while True:
        try:
            n=int(input())
            if n>0: return n
        except ValueError:
            pass
        print('Valore non valido, riprova!')

def gioca_turno(giocatore):
    print(f'Turno di {giocatore}')
    comb=dadi.lancia_dadi()
    scelta=input('Vuoi rilanciare alcuni dadi? (si/no) : ')
    if scelta.lower()=='si':
        comb=dadi.cambia_dadi(comb)
    valutata = dadi.valuta_combinazione(comb)
    return calcola_punteggio(valutata)

def calcola_punteggio(combinazione):
    punti_classici={'yahtzee': 50,
                    'poker': 40,
                    'full': 30,
                    'scala': 25,
                    'tris': 20,
                    'doppia coppia': 15,
                    'coppia': 10,
                    'nulla': 0}
    punti=punti_classici[combinazione[0]]+combinazione[1]
    return punti

def classifica(giocatori):
    classifica=list(sorted(giocatori.items(),key = lambda x : x[1], reverse=True))
    return classifica

def crea_file_classifica(classifica):
    with open('dati.txt', mode='w') as f:
        file = ' Classifica Torneo:'
        for classificato in classifica:
            file+=f'\n {classificato[0]}: {classificato[1]} punti'
        f.write(file)


#print(gioca_turno('Dennis'))