import csv
import random


def dane_klienta():
    imie = input("Podaj imię i nazwisko: ")
    email = input("Podaj adres e-mail: ")
    telefon = input("Podaj numer telefonu: ")
    ulica = input("Podaj ulice: ")
    miasto = input("Podaj miasto: ")
    kraj = input("Podaj kraj")
    return imie, email, telefon, ulica, miasto, kraj


def dodaj_klienta(fun):
    imie, email, telefon, ulica, miasto, kraj = fun
    id = random.randint(1000, 9999)
    with open('customer.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([id, imie, email, telefon])
    print("Nowy klient dodany do bazy.")
    with open('address.csv', 'a', newline='', encoding='utf-8') as file1:
        write = csv.writer(file1)
        write.writerow([id, ulica, miasto, kraj])


# dodaj_klienta(dane_klienta())