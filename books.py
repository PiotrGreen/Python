import csv


def dodaj_ksiazke(id, autor, tytul, liczba_stron, data_wydania):
    """
    Dodaje nową książkę do pliku CSV.

    Args:
        id (int): Identyfikator książki.
        autor (str): Autor książki.
        tytul (str): Tytuł książki.
        liczba_stron (int): Liczba stron książki.
        data_wydania (str): Data wydania ksiązki
    """
    with open('book.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([id, autor, tytul, liczba_stron, data_wydania])
    print("Książka dodana pomyślnie do bazy.")


# Przykładowe użycie
# dodaj_ksiazke(106, "Paweł Nowak", "Python", 90, "02.10.2021")


def usun_ksiazke(identyfikator, opcja):
    """
    Usuwa książkę z bazy na podstawie ID lub tytułu.

    Args:
        identyfikator (str or int): ID lub tytuł książki do usunięcia.
        opcja (str): 'id' lub 'tytuł', domyślnie 'id'.
    """
    with open('book.csv', 'r', newline='', encoding='utf-8') as file:
        rows = list(csv.reader(file))

    if opcja == 'id':
        for row in rows:
            if row[0] == str(identyfikator):
                rows.remove(row)
                break
    elif opcja == 'tytuł':
        for row in rows:
            if row[2] == str(identyfikator):
                rows.remove(row)
                break
    else:
        print("Nieprawidłowa opcja.")
        return

    with open('book.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("Książka usunięta pomyślnie z bazy.")


# Przykładowe użycie
# usun_ksiazke(104, 'id')  # Usuwa książkę o ID = 1
# usun_ksiazke("Promocje w Lidlu", 'tytuł')
