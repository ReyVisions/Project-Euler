import time
import math



def main():
    start_time1 = time.time()

    collection=set()

    for a in range(2,101):
        for b in range(2,101):
            collection.add(a**b)

    print(len(collection))
    end_time1 = time.time()

    # Calcul du temps écoulé
    elapsed_time1 = end_time1 - start_time1
    print(f"Le code a pris {elapsed_time1:.5f} secondes à s'exécuter.")

    return 0

if __name__ == '__main__':
    main()