#avvia il torneo
import utils
import torneo
def start():
    print('🎲 Benvenuti al torneo di dadi 2025')
    n=utils.scegli_numero_giocatori()
    giocatori=utils.scegli_giocatori(n)
    turni=torneo.scegli_turni()
    punteggi={}
    for giocatore in giocatori:
        punteggi[giocatore]=0
    for _ in range(turni):
        for giocatore in giocatori:
            punteggi[giocatore]+=torneo.gioca_turno(giocatore)
    classifica = torneo.classifica(punteggi) 
    print(f'Il vincitore è {classifica[0][0]} con un punteggio di {classifica[0][1]}')
    torneo.crea_file_classifica(classifica)
    return classifica

if __name__=='__main__':
    print(start())