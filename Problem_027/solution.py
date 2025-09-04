import time
import math


def is_prime(n):
    if n<=0:
        return(False)
    if n==1:
        return(False)
    if n==2:
        return(True)
    for i in range(2,int(n**(1/2))):
        if n%i==0:
            return(False)
    return(True)

def f(x,a,b):
    return(x**2+a*x+b)


def main():
    start_time1 = time.time()
    
    max=0
    for b in range(0,1000):
        for a in range(-b,1000):
            for n in range(1000):
                if not is_prime(f(n,a,b)):
                    break
            if n>max:
                max=n
                amax=a
                bmax=b

    print(max,n,amax,bmax)



    end_time1 = time.time()

    # Calcul du temps écoulé
    elapsed_time1 = end_time1 - start_time1
    print(f"Le code a pris {elapsed_time1:.5f} secondes à s'exécuter.")

    return 0

if __name__ == '__main__':
    main()