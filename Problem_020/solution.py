import sys
import time
import math
         



def main():

    start_time1 = time.time()
    n=str(math.factorial(100))
    somme=0
    for i in range(len(n)):
        somme+=int(n[i])
    print(somme)
    
    end_time1 = time.time()


    elapsed_time1 = end_time1 - start_time1
    print(f"Le code naif a pris {elapsed_time1:.5f} secondes à s'exécuter.")

    return(0)

if __name__ == '__main__':
    sys.exit(main())