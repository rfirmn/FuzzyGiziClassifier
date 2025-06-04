import numpy as np


from fuzzy_logic.mamdani_7 import fuzzy_mamdani_7
from fuzzy_logic.sugeno_7 import fuzzy_sugeno_7
from fuzzy_logic.mamdani_8 import fuzzy_mamdani_8
from fuzzy_logic.sugeno_8 import fuzzy_sugeno_8
from fuzzy_logic.mamdani_9 import fuzzy_mamdani_9
from fuzzy_logic.sugeno_9 import fuzzy_sugeno_9
from fuzzy_logic.mamdani_10 import fuzzy_mamdani_10
from fuzzy_logic.sugeno_10 import fuzzy_sugeno_10


def main():
    berat = int(input("Berapa berat mu: "))
    tinggi = int(input("Berapa tinggi mu:"))
    umur = 7
    

    if umur == 7:

        mamdani_output = fuzzy_mamdani_7(berat, tinggi)
        sugeno_output = fuzzy_sugeno_7(berat, tinggi)
        print(f"Mamdani: {mamdani_output:.3f}; Sugeno: {sugeno_output:.3f}")

    elif umur == 8:
        for i in range(20):
            mamdani_output = fuzzy_mamdani_8(berat[i], tinggi[i])
            sugeno_output = fuzzy_sugeno_8(berat[i], tinggi[i])
            print(f"Mamdani: {mamdani_output:.3f}; Sugeno: {sugeno_output:.3f}")
            
    elif umur == 9:
        for i in range(20):
            mamdani_output = fuzzy_mamdani_9(berat[i], tinggi[i])
            sugeno_output = fuzzy_sugeno_9(berat[i], tinggi[i])
            print(f"Mamdani: {mamdani_output:.3f}; Sugeno: {sugeno_output:.3f}")
            
    elif umur == 10:
        for i in range(20):
            mamdani_output = fuzzy_mamdani_10(berat[i], tinggi[i])
            sugeno_output = fuzzy_sugeno_10(berat[i], tinggi[i])
            print(f"Mamdani: {mamdani_output:.3f}; Sugeno: {sugeno_output:.3f}")


if __name__ == "__main__":
    main()
