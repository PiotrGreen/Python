from books import *
from customers import *
import random


def main1():
    co_robic = input("Co chesz zrobić? \n"
                     "1 Dodać książkę. \n"
                     "2 Usunać książkę. \n"
                     "3 Dodać klienta. \n"
                     "4 Usunąć klienta. ")
    if co_robic == "1":
        id = random.randint(1000, 9999)
        autor = input("Podaj autora. ")
        tytul = input("Podaj tytuł. ")
        liczba_stron = int(input("Podaj liczbe stron. "))
        data_dodania = date.today()
        dodaj_ksiazke(id, autor, tytul, liczba_stron, data_dodania)
    elif co_robic == "2":
        opcja = input("Według czego usunać książke id lub tytuł? ")
        identyfikator = input("Co wybrałes to to podaj. ")
        usun_ksiazke(identyfikator, opcja)
    elif co_robic == "3":
        dodaj_klienta(dane_klienta())
    else:
        print("Ta opcja narazie nie dostępna.")


if __name__ == "__main__":
    main1()
