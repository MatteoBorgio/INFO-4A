# 1
SIMBOLO_EURO = '\u20AC'

def sconto_primo_negozio(spesa: float) -> float:
    if spesa <= 0:
        raise ValueError(f"La spesa deve essere maggiore di 0{SIMBOLO_EURO}")
    if spesa < 500:
        sconto = spesa * 10 / 100
        importo_finale = spesa - sconto
    else:
        sconto = spesa * 20 / 100
        importo_finale = spesa - sconto
    print(f"""Alla spesa di {spesa}{SIMBOLO_EURO} è stato applicato lo sconto di {sconto}{SIMBOLO_EURO}
Importo finale: {importo_finale}{SIMBOLO_EURO}""") 
    return importo_finale   

# 2
def sconto_secondo_negozio(spesa: float) -> float:
    if spesa <= 0:
        raise ValueError(f"La spesa deve essere maggiore di 0{SIMBOLO_EURO}")
    if spesa <= 300:
        sconto = spesa * 10 / 100
        importo_finale = spesa - sconto
    else:
        primo_sconto_parziale = 30
        importo_parziale = spesa - 300
        secondo_sconto_parziale = importo_parziale * 20 / 100
        sconto = primo_sconto_parziale + secondo_sconto_parziale
        importo_finale = spesa - sconto
    print(f"""Alla spesa di {spesa}{SIMBOLO_EURO} è stato applicato lo sconto di {sconto}{SIMBOLO_EURO}
Importo finale: {importo_finale}{SIMBOLO_EURO}""")     
    return importo_finale

if __name__ == "__main__":
    while True:
        try:
            spesa = float(input("Inserisci un valore di spesa valido: "))
            break
        except:
            print("Valore di spesa non valido!")
    importo_primo_negozio = sconto_primo_negozio(spesa)
    importo_secondo_negozio = sconto_secondo_negozio(spesa)
    if importo_primo_negozio < importo_secondo_negozio:
        print("Il negozio più conveniente con questa spesa è il primo negozio")
    elif importo_secondo_negozio < importo_primo_negozio:
        print("Il negozio più conveniente con questa spesa è il secondo negozio")
    else:   
        print("Con questa spesa la scelta del negozio è indifferente")