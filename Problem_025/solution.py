import time
import math

def main():
    start_time1 = time.time()
    a=1
    b=1
    index=2
    while len(str(b))<1000:
        a,b=b,b+a
        index+=1
    print(index)


    end_time1 = time.time()

    # Calcul du temps écoulé
    elapsed_time1 = end_time1 - start_time1
    print(f"Le code a pris {elapsed_time1:.5f} secondes à s'exécuter.")

    return 0

if __name__ == '__main__':
    main()