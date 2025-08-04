# 🥂 Simulatore di Bar per Cocktail

Questo è un progetto Python che simula il funzionamento di un bar specializzato in cocktail. 
Gestisce ricette, magazzino, ordinazioni, vendite e prezzi in modo dinamico.

## 📁 Struttura del progetto

cocktail_bar/
│
├── main.py # Avvia il simulatore
├── bar.py # Logica per gestione ordinazioni e vendite
├── cocktail.py # Classe Cocktail: gestisce nome, ingredienti e ricette
├── magazzino.py # Gestione scorte e rifornimenti
├── vendite.py # Report vendite
├── tipi_ingredienti.py # Dizionario ingredienti → tipo (alcol/allungante)
├── cliente.py #Verifica cocktail accessibili in base al budget cliente e gestisce ordine e pagamento
│
├── dati/ # Cartella dei file di dati
│ ├── ricette.json # Ricette dei cocktail
│ ├── scorte.json # Scorte disponibili in magazzino
│ └── vendite.csv # Registro vendite (generato automaticamente)
| └── prezzi.json # contiene un dizionario che ha per chiave il nome del cocktail e per valore il prezzo
---

## 🧠 Funzionalità principali

- ✅ Creazione cocktail da ricetta esistente o input utente
- ✅ Verifica delle scorte prima di servire
- ✅ Rifornimento magazzino in caso di ingredienti insufficienti
- ✅ Calcolo dinamico dei prezzi basato sul tipo di ingredienti (se non è già presente un file prezzi)
- ✅ Registrazione automatica delle vendite
- ✅ Report delle vendite totali in euro
- ✅ Supporto a un vasto set di cocktail internazionali con quantità secondo standard IBA

---

## ▶️ Come eseguire il progetto

### 🔧 Requisiti

- Python 3.8 o superiore

### ▶️ Esecuzione
# NOTA: puoi modificare i file prezzi.json, scorte.json e ricette.json e salvare, ma dovrai mantenere la stessa logica contenuta in essi per un corretto funzionamento
1. Clona il progetto o scaricalo come `.zip`
2. Assicurati che la cartella `dati/` contenga i file `ricette.json`, `prezzi.json`, `scorte.json` e `vendite.csv`
3. Assicurati di essere nella cartella principale del progetto
4. Avvia il programma da terminale (alternativamente esegui il main.py su VSCode o simili):
```bash 
python main.py

📌 Esempio di output

         MENU           
| Nome cocktail | Prezzo |
-------------------------
| Margarita | 5.0|
| Mojito | 5.0|
| Daiquiri | 3.5|
| Cosmopolitan | 6.0|
| Negroni | 7.0|
| Americano | 5.5|
| Gin Tonic | 3.5|
| Vodka Lemon | 3.5|
| Gin Lemon | 4.0|
| Whiskey Sour | 4.0|
| Mai Tai | 8.0|
| Long Island Iced Tea | 9.0|
| Caipirinha | 2.0|
| Caipiroska | 4.0|
| Pina Colada | 2.0|
| Cuba Libre | 2.0|
| Tequila Sunrise | 3.5|
| Bloody Mary | 4.0|
| Sex On The Beach | 4.5|
| Espresso Martini | 3.5|
| Aperol Spritz | 4.5|
| Black Russian | 3.5|
| White Russian | 3.5|
| Irish Coffee | 2.0|
| Tom Collins | 5.0|
| Clover Club | 5.0|
| French 75 | 6.5|
| Aviation | 4.0|
| Manhattan | 4.5|
| Old Fashioned | 4.0|
| Mint Julep | 4.5|
| Planter'S Punch | 6.0|
| Sea Breeze | 4.0|
| Bay Breeze | 4.5|
| Harvey Wallbanger | 5.0|
| Bramble | 4.5|
| Paloma | 4.0|
| Boulevardier | 7.5|
| Sidecar | 5.0|
| Bellini | 4.0|
| Negroni Sbagliato | 6.0|
| Screwdriver | 3.0|
| Rusty Nail | 5.5|
| Godfather | 5.5|
| Grasshopper | 6.0|
| Alexander | 5.5|
_____________________

--- Cliente 1 (budget iniziale: €19.40) ---
[Cliente 1] Ordina: Aviation
Aviation venduto a €4.0.
[Cliente 1] Ordina: Sea Breeze
❌ Non ci sono scorte sufficienti per preparare Sea Breeze.
Ingredienti richiesti: {'vodka': 4, 'succo di mirtillo': 12, 'succo di pompelmo': 3}
🔄 Rifornimento automatico in corso...
➕ Rifornite 2 bottiglie di succo di pompelmo.

--- Cliente 2 (budget iniziale: €15.65) ---
[Cliente 2] Ordina: Old Fashioned
Old Fashioned venduto a €4.0.

--- Cliente 3 (budget iniziale: €13.12) ---
[Cliente 3] Ordina: Vodka Lemon
Vodka Lemon venduto a €3.5.

--- Cliente 4 (budget iniziale: €12.67) ---
[Cliente 4] Ordina: Godfather
Godfather venduto a €5.5.
[Cliente 4] Ordina: Caipiroska
Caipiroska venduto a €4.0.

--- FINE GIORNATA ---

Registro vendite:
-----------------
Aviation: €4.0
Old Fashioned: €4.0
Vodka Lemon: €3.5
Godfather: €5.5
Caipiroska: €4.0
-------------
Totale vendite: €21.00
```

### 📈 Espandibilità
- Questo progetto è pensato per essere facilmente esteso:

- Aggiunta di interfaccia grafica (Tkinter, PyQt)

- Statistiche avanzate sui cocktail più venduti

- Sistema di login per barman/manager

- Integrazione con database SQLite

### 🧑‍💻 Autore
Progetto ideato e sviluppato da Dennis Acconcio come esercizio di programmazione Python + gestione dati.

### 📝 Licenza
Questo progetto è distribuito sotto la licenza MIT.
Sentiti libero di modificarlo e migliorarlo!