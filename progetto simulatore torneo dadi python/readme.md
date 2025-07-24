# 🎲 Torneo di Dadi 2025

Un progetto in Python che simula un torneo di dadi tra più giocatori, con lancio, rilancio e valutazione automatica delle combinazioni. Alla fine viene generata una classifica e salvata in un file di testo.

---

## 📦 Struttura del progetto

torneo_dadi/
├── main.py # Avvia il torneo e gestisce il flusso principale
├── torneo.py # Gestione dei turni, punteggi, classifica e salvataggio file
├── dadi.py # Lancio dadi, rilanci e valutazione delle combinazioni
├── utils.py # Funzioni di supporto per input e validazioni
└── dati.txt # File generato automaticamente con la classifica finale

---

## ▶️ Come funziona

1. L'utente sceglie il numero di giocatori e inserisce i loro nomi.
2. Viene chiesto quanti turni giocare.
3. Ogni giocatore, a ogni turno:
   - Lancia 5 dadi.
   - Può decidere se rilanciare alcuni dadi.
   - Ottiene un punteggio in base alla combinazione.
4. Alla fine del torneo viene mostrata la classifica.
5. I risultati vengono salvati nel file `dati.txt`.

---

## 🧠 Combinazioni e punteggi

| Combinazione      | Punti base | Valore aggiuntivo |
|-------------------|------------|--------------------|
| Yahtzee (5 uguali) | 50         | valore del dado    |
| Poker (4 uguali)   | 40         | valore del dado    |
| Full (3+2)         | 30         | valore del tris    |
| Scala (1-5 o 2-6)  | 25         | valore finale (5 o 6) |
| Tris (3 uguali)    | 20         | valore del tris    |
| Doppia coppia      | 15         | valore della coppia più alta |
| Coppia             | 10         | valore della coppia |
| Nulla              | 0          | valore massimo dei dadi |

---

## 📄 Esempio di output

🎲 Benvenuti al torneo di dadi 2025
Scegli il numero di giocatori che partecipano alla sfida: 2
Nome giocatore 1: Dennis
Nome giocatore 2: Manuel
Quanti turni volete disputare? (Almeno 1)
3

Turno di Dennis
La tua combinazione è: [2, 2, 3, 6, 1]
Vuoi rilanciare alcuni dadi? (si/no) : si
Scegli quali dadi vuoi rilanciare (uno alla volta seguiti da ENTER/INVIO), digita q per terminare.
2
4
q
La tua combinazione finale è: [2, 5, 3, 2, 1]

...

Il vincitore è Dennis con un punteggio di 127

---

## 💾 Output generato

Alla fine viene creato un file `dati.txt` contenente:

Classifica Torneo:
Dennis: 127 punti
Manuel: 113 punti

---

## ⚙️ Requisiti

- Python 3.x
- Nessuna libreria esterna necessaria

---

## 📚 Obiettivo didattico

Questo progetto è stato realizzato per mettere in pratica:
- Funzioni, cicli, condizioni e input
- Liste, dizionari e Counter
- Uso di moduli e struttura in più file
- Lettura/scrittura file
- Progettazione procedurale senza OOP

---

## 👨‍💻 Autore

Creato da Dennis Acconcio

---