import csv
from collections import Counter
from itertools import chain
import os

# nejdříve načte soubor s daným názvem (v základu "vstup.csv") a vrací (returns) a tiskne (print) nejvíce se vyskytující element a jeho frekvenci
# poté to seznamy seznamů změní na jeden větší seznam (chain) a poté seřadí a pomocí Counter počítá frekvence jednotlivých prvků v "data" (náš seřazený a velký seznam)
# most_common hledá prvek co se objevuje nejčastěji (=modus), frquency frekvenci tohoto prvku
# print vytiskne prvek, který je v souboru nejčastěji (= modus) a jeho četnost
# return zde není vyloženě potřeba, ale kdybychom nechtěli jen vypsat modus, ale i s ním nějak dál počítat, tak by se return hodil.
# v posledních řádcích probíhá exekuce celé funkce (a u tohoto programu i celého programu)

# třída pro výjimku prázdného souboru. Chtěl jsem se vyhnout užití knihovny pandas, když není ve VS Code defaultně a musí se stáhnout
class EmptyFileException(Exception):
    def __init__(self, message):
        self.message = message

def find_most_common_element(input_file):
    try:
        with open(input_file, 'r') as input_file:
            if os.stat("vstup.csv").st_size == 0:
                raise EmptyFileException("Vstupní soubor je prázdný.")
            reader = csv.reader(input_file)
            data = [row for row in reader]
    except FileNotFoundError:
        print("Vstupní soubor nebyl nalezen.")
        exit(1)
    except EmptyFileException as EmptyError:
        print(EmptyError)
        exit(1)

    data = sorted(chain(*data))
    c = Counter(data)

    most_common, frequency = c.most_common(1)[0]

    print(f"Prvek, ktery se v souboru vyskytoval nejcasteji byl: {most_common}")
    print(f"Tento prvek (=modus) se v souboru vyskytl {frequency}xkrát.")
    return (most_common, frequency)

most_common, frequency = find_most_common_element('vstup.csv')