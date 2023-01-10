import csv
from collections import Counter
from itertools import chain
import os

# nejdrive nacte soubor s danym nazvem (v zakladu "vstup.csv") a vraci (returns) a tiskne (print) nejvíce se vyskytující element a jeho frekvenci, vraci ten input jako "data"
# pote to seznamy seznamu zmeni na jeden vetsi seznam (chain) a pote seradi a pomoci Counter pocita frekvence jednotlivych prvku v "data_sorted" (nas serazeny  velky seznam)
# most_common hleda prvek co se objevuje nejcasteji (=modus), frequency hleda frekvenci tohoto prvku
# print vytiskne prvek, ktery je v souboru nejcasteji (= modus) a jeho cetnost
# v poslednich radcich probiha exekuce cele funkce (a u tohoto programu i celeho programu)

# trida pro vyjimku prazdneho souboru. Chtel jsem se vyhnout uziti knihovny pandas, kdyz to neni defaultni knihovna a musi se stahnout
class EmptyFileException(Exception):
    def __init__(self, message):
        self.message = message

def open_file(input_file):
    try:
        with open(input_file, 'r') as input_file:
            if os.stat("vstup.csv").st_size == 0:
                raise EmptyFileException("Vstupni soubor je prazdny.")
            reader = csv.reader(input_file)
            data = [row for row in reader]
    except FileNotFoundError:
        print("Vstupni soubor nebyl nalezen.")
        exit(1)
    except EmptyFileException as EmptyError:
        print(EmptyError)
        exit(1)
    return data

def modus_calculation(data):
    data_sorted = sorted(chain(*data))
    c = Counter(data_sorted)

    most_common, frequency = c.most_common(1)[0]

    print(f"Prvek, ktery se v souboru vyskytoval nejcasteji byl: {most_common}")
    print(f"Tento prvek (=modus) se v souboru vyskytl {frequency}xkrát.")

def main():
    data = open_file("vstup.csv")
    modus_calculation(data)

main()