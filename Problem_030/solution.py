import time
import math



def main():
    start_time1 = time.time()

    sum=0
    L=[]
    for i in range(2,1000000):
        temp_sum=0
        for j in str(i):
            temp_sum+=int(j)**5
        if temp_sum==i:
            sum+=i
            L.append(i)
            
    print(sum)
    print(L)

    end_time1 = time.time()

    # Calcul du temps écoulé
    elapsed_time1 = end_time1 - start_time1
    print(f"Le code a pris {elapsed_time1:.5f} secondes à s'exécuter.")

    return 0

if __name__ == '__main__':
    main()