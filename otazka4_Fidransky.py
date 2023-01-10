import re
import os

# Nejdrive promenna string odstrani nevhodne symboly, ktere by se v tabulce pletly - predevsim ",", ".", "?", "!". Respektive
# to odstrani všechny symboly, ktere nejsou v abecede nebo to nejsou cisla
# Pote se vytvori prazdny slovnik, pote se spusti for cyklus, dlouhy podle delky inputu. Pokud uz znak byl nekdy zapocitan (= objevil se v stringu drive),
# tak se pricte +1, pokud ne, tak se mu prideli 1. To se provadi znovu do te doby, nez se ukonci for cyklus (= dojede na konec inputu).
# char_freq se pote seradi podle cetnosti znaku, tedy pokud se napr. "u" vyskytlo 4x a "b" 3x, tak "u" bude prvni, ac abecedne by bylo druhe
# poslední for cyklus tiskne znaky, opet dokud nevypise vsechny znaky co se objevily v inputu.
# ve funkci main se spouští while cyklus, který ve finále nutí uživatele, aby něco zadal (bude se ptát znovu, dokud uživatel něco nezadá)

def char_freq(string):
  string = string.upper()
  char_freq = {}

  for char in string:
    if char != " ":
      if char not in char_freq:
        char_freq[char] = 1
      else:
        char_freq[char] += 1

  char_freq = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)

  for char, freq in char_freq:
    print(f"{char}: {freq}")

def main():
  while True:
    string = input("Zadejte větu, u které chcete zjistit frekvenci: ")
    if string.strip() != "":
        char_freq(string)
        break
    else:
        print("Vstup nebyl zadán, zkuste to znovu.")


main()