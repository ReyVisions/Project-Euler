import time
import math



def main():
    start_time1 = time.time()

    n=6
    last_number=25
    sum=101
    while n<1001:
        for i in range(4):
            last_number+=n
            sum+=last_number
        n+=2

    print(sum)

    end_time1 = time.time()

    # Calcul du temps écoulé
    elapsed_time1 = end_time1 - start_time1
    print(f"Le code a pris {elapsed_time1:.5f} secondes à s'exécuter.")

    return 0

if __name__ == '__main__':
    main()