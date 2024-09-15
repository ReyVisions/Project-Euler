import sys
import time
import math


def main():
    # Commencer la mesure de temps
    start_time1 = time.time()

    print(math.comb(40,20))

    # Fin de la mesure de temps
    end_time1 = time.time()

    # Calcul du temps écoulé
    elapsed_time1 = end_time1 - start_time1
    print(f"Le code naif a pris {elapsed_time1:.5f} secondes à s'exécuter.")

    return(0)

if __name__ == '__main__':
    sys.exit(main())