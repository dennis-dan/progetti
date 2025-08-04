def report_vendite(percorso_file='dati/vendite.csv'):
    print()
    print("Registro vendite:")
    print('-----------------')
    
    amount = 0
    try:
        with open(percorso_file, encoding='utf-8') as f:
            righe = [riga.strip() for riga in f if riga.strip()]  # elimina righe vuote
    except FileNotFoundError:
        print("Nessun file vendite trovato.")
        return "Totale vendite: €0.00"
    
    if not righe:
        print("Nessuna vendita registrata.")
        return "Totale vendite: €0.00"
    
    for riga in righe:
        try:
            nome, prezzo = riga.split(',')
            prezzo = float(prezzo)
            print(f"{nome}: €{prezzo}")
            amount += prezzo
        except ValueError:
            print(f"Riga malformattata ignorata: {riga}")
    
    print('-------------')
    return f"Totale vendite: €{amount:.2f}"
