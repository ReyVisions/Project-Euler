import sys
import time

def collatz(n):
    if n%2==0:
        n=n//2
    else:
        n=3*n+1
    return(n)

def longest_collatz_naive(n):
    list=[]
    size=1
    last=0
    for i in range(1,n+1):
        last=i
        size=1
        while last>1:
            last=collatz(last)
            size+=1
        list.append(size)
    return(list.index(max(list))+1)
 

def longest_collatz_optimized(n):
    dictionnary={}
    dictionnary[1]=1
    list=[]
    size=1
    last=0
    for i in range(2,n+1):
        list=[]
        last=i
        size=1
        while last>1:
            if dictionnary.get(last)==None:
                list.append(last)
                last=collatz(last)
            else:
                last=1
        while len(list)>0:
            size2=dictionnary.get(collatz(list[-1]))
            dictionnary[list[-1]]=size2+1
            list.pop(-1)
            size+=1
            last=1

    maxi=max(dictionnary,key=dictionnary.get)
    return(maxi)


def main():
    # Commencer la mesure de temps
    start_time1 = time.time()

    print(longest_collatz_naive(1000000))
    # Fin de la mesure de temps
    end_time1 = time.time()
    # Commencer la mesure de temps
    start_time2 = time.time()
    print(longest_collatz_optimized(1000000))
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