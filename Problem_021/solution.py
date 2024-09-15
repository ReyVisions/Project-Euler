import sys
import time
import math
         



def main():

    start_time1 = time.time()
    overall=0
    sum1=0
    sum2=0
    for n in range(10000):
        sum1=0
        sum2=0
        for i in range(1,int(n**(1/2))+2):
            if n%i==0:
                if i!=n//i and i!=1:
                    print(i)
                    sum1+=i
                    print(n//i)
                    sum1+=n//i
                else:
                    print(i)
                    sum1+=i
        for i in range(1,int(sum1**(1/2))+2):
            if sum1%i==0:
                if i!=sum1//i and i!=1:
                    sum2+=i
                    sum2+=sum1//i
                else:
                    sum2+=i
        if sum2==n and sum1!=sum2:
            overall+=n
        print(n,sum1)
    print(overall)
    
    end_time1 = time.time()


    elapsed_time1 = end_time1 - start_time1
    print(f"Le code naif a pris {elapsed_time1:.5f} secondes à s'exécuter.")

    return(0)

if __name__ == '__main__':
    sys.exit(main())