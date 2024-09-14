import sys
import time




def main():
    # Commencer la mesure de temps
    start_time1 = time.time()


    # Fin de la mesure de temps
    end_time1 = time.time()
    # Commencer la mesure de temps
    start_time2 = time.time()


    # Fin de la mesure de temps
    end_time2 = time.time()

    # Calcul du temps écoulé
    elapsed_time1 = end_time1 - start_time1
    print(f"Le code naif a pris {elapsed_time1:.5f} secondes à s'exécuter.")
    # Calcul du temps écoulé
    elapsed_time2 = end_time2 - start_time2
    print(f"Le code optimise a pris {elapsed_time2:.5f} secondes à s'exécuter.")
    return(0)

if __name__ == '__main__':
    sys.exit(main())