import time
import math



def main():
    start_time1 = time.time()
    sum=0
    for a in range(10,100):
        for b in range(a,100):
            for i in range(2,min(a,b)+1,-1):
                if a%i==0 and b%i==0:
                    break
                if i==min(a,b):
                    sum+=a
    print(sum)

    end_time1 = time.time()

    # Calcul du temps écoulé
    elapsed_time1 = end_time1 - start_time1
    print(f"Le code a pris {elapsed_time1:.5f} secondes à s'exécuter.")

    return 0

if __name__ == '__main__':
    main()