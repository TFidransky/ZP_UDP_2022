import csv
from collections import Counter
from itertools import chain
# nejdříve načte soubor s daným názvem (v základu "vstup.csv") a vrací (returns) a tiskne (print) nejvíce se vyskytující element a jeho frekvenci
# poté to seznamy seznamů změní na jeden větší seznam (chain) a poté seřadí a pomocí Counter počítá frekvence jednotlivých prvků v "data" (náš seřazený a velký seznam)
# most_common hledá prvek co se objevuje nejčastěji (=modus), frquency frekvenci tohoto prvku
# print vytiskne prvek, který je v souboru nejčastěji (= modus) a jeho četnost
# return zde není vyloženě potřeba, ale kdybychom nechtěli jen vypsat modus, ale i s ním nějak dál počítat, tak by se return hodil.
# v posledních řádcích probíhá exekuce celé funkce (a u tohoto programu i celého programu)

def find_most_common_element(input_file):
    with open(input_file, 'r') as input_file:
        reader = csv.reader(input_file)
        data = [row for row in reader]

    data = sorted(chain(*data))
    c = Counter(data)

    most_common, frequency = c.most_common(1)[0]

    print(f"Prvek, ktery se v souboru vyskytoval nejcasteji byl: {most_common}")
    print(f"Tento prvek (=modus) se v souboru vyskytl {frequency}xkrát.")
    return (most_common, frequency)

most_common, frequency = find_most_common_element('vstup.csv')
