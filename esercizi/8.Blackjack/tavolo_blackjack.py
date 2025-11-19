from mazzo import Mazzo
from mano import Mano
from carta import Carta

class TavoloBlackjack:
    def __init__(self):
        self.__mazzo = Mazzo(self.__crea_mazzo_standard())
        self.__mazzo.mescola()
        self.__mano_giocatore = Mano()
        self.__mano_banco = Mano()
        self.__turno_giocatore_finito = False
        self.__turno_banco_finito = False

    def __crea_mazzo_standard(self) -> list:
        semi = ["Cuori", "Picche", "Fiori", "Quadri"]
        ranghi = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        mazzo = []
        for seme in semi:
            for rango in ranghi:
                mazzo.append(Carta(seme, rango))
        return mazzo
    
    def __calcola_punteggio(self, mano_obj: Mano) -> int:
        carte = mano_obj.get_carte()
        valore_mano = 0
        num_assi = 0
        for carta in carte:
            try:
                if carta.rango == "A":
                    num_assi += 1 
            except AttributeError:
                raise ValueError("L'oggetto non è una carta valida!")
            try:
                valore_mano += carta.valore
            except AttributeError:
                raise ValueError("L'oggetto non è una carta valida!")
        while valore_mano > 21 and num_assi > 0:
            valore_mano -= 10
            num_assi -= 1
        return valore_mano
    
    def __turno_giocatore(self) -> None:
        while True:
            try:
                input_utente = input("Chiedi (C) o Stai (S): ")
                if input_utente.upper() not in ["C", "S"]:
                    raise ValueError
                break
            except ValueError:
                print("Inserisci un input valido (C o S)")
        if input_utente.upper() == "C":
            carta = self.__mazzo.pesca()
            self.__mano_giocatore.aggiungi_carta(carta)
            print(f"Hai pescato {carta}")
            print(f"Valore attuale mano: {self.__calcola_punteggio(self.__mano_giocatore)}")
        else:
            self.__turno_giocatore_finito = True
        
    def __turno_banco(self) -> None:
        if self.__calcola_punteggio(self.__mano_banco) <= 16:
            carta = self.__mazzo.pesca()
            self.__mano_banco.aggiungi_carta(carta)
            print(f"Il banco ha pescato {carta}")
            print(f"Valore attuale mano: {self.__calcola_punteggio(self.__mano_banco)}")
        else: 
            self.__turno_banco_finito = True

    def __calcola_vittoria(self) -> None:
        if self.__mano_giocatore.carte == []:
            print("Hai sballato!")
            return
        if self.__mano_banco.carte == []:
            print("Il banco ha sballato! Hai vinto!")
            return
        if self.__calcola_punteggio(self.__mano_banco) >= self.__calcola_punteggio(self.__mano_giocatore):
            print("Hai perso!")
        else:
            print("Hai vinto")

    def gioca_partita(self) -> None:
        prima_carta_banco = self.__mazzo.pesca()
        self.__mano_banco.aggiungi_carta(prima_carta_banco)
        self.__mano_giocatore.aggiungi_carta(self.__mazzo.pesca())
        self.__mano_banco.aggiungi_carta(self.__mazzo.pesca())
        self.__mano_giocatore.aggiungi_carta(self.__mazzo.pesca())
        print(f"Il giocatore ha pescato {self.__mano_giocatore}")
        print(f"La prima carta pescata dal banco è {prima_carta_banco}")
        while self.__turno_giocatore_finito == False:
            if self.__calcola_punteggio(self.__mano_giocatore) == 21:
                break
            if self.__calcola_punteggio(self.__mano_giocatore) > 21:
                self.__mano_giocatore.svuota()
                self.__calcola_vittoria()
                return
            self.__turno_giocatore()
        print(f"La mano del banco è: {self.__mano_banco}")
        while self.__turno_banco_finito == False:
            if self.__calcola_punteggio(self.__mano_banco) == 21 or self.__calcola_punteggio(self.__mano_banco) >= self.__calcola_punteggio(self.__mano_giocatore):
                break
            if self.__calcola_punteggio(self.__mano_banco) > 21:
                self.__mano_banco.svuota()
                self.__calcola_vittoria()
                return
            self.__turno_banco()
        self.__calcola_vittoria()

if __name__ == "__main__":
    tavolo = TavoloBlackjack()
    tavolo.gioca_partita()
        