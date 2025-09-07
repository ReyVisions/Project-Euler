import time
import math



def main():
    start_time1 = time.time()

    sum=0
    chain=''
    L=[1,2,3,4,5,6,7,8,9]
    for i in L:
        chain+=str(L)

    end_time1 = time.time()

    # Calcul du temps écoulé
    elapsed_time1 = end_time1 - start_time1
    print(f"Le code a pris {elapsed_time1:.5f} secondes à s'exécuter.")

    return 0

if __name__ == '__main__':
    main()