import time
import math

def main():
    start_time1 = time.time()
    

    for i in range(1,1000):
        print(str(1/i)[2:])
        for j in str(1/i)[2:]:
            pass



    end_time1 = time.time()

    # Calcul du temps écoulé
    elapsed_time1 = end_time1 - start_time1
    print(f"Le code a pris {elapsed_time1:.5f} secondes à s'exécuter.")

    return 0

if __name__ == '__main__':
    main()