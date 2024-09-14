import sys
import time
import math

def optimized():
    sum = 0
    for n in str(2**1000):
        sum += int(n)
    return sum

def main():
    # Commencer la mesure de temps
    start_time1 = time.time()
    a=1
    for i in range(1000):
        a*=2
    print(a)
    seq=str(a)
    sum=0
    for i in seq:
        sum+=int(i)
    print(sum)

    # Fin de la mesure de temps
    end_time1 = time.time()

    # Calcul du temps écoulé
    elapsed_time1 = end_time1 - start_time1
    print(f"Le code naif a pris {elapsed_time1:.5f} secondes à s'exécuter.")

    return(0)

if __name__ == '__main__':
    sys.exit(main())