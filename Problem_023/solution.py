import time

def main():
    start_time1 = time.time()

    sum=0
    abondants=[]
    sum_non_abondants=0
    for n in range(1,28123):
        sum=0
        for i in range(1,int(n**(1/2))+1):
            if n%i==0:
                if i!=n//i and i!=1:
                    sum+=i
                    sum+=n//i
                else:
                    sum+=i
        if sum>n:
            abondants.append(n)
    print(abondants)
    for i in range(28123):
        for j in range(len(abondants)):
            if i>abondants[j]:
                copy=i
                copy-=abondants[j]
                if copy not in abondants:
                    sum_non_abondants+=i
            else:
                sum_non_abondants+=i
                break
    print(sum_non_abondants)


    end_time1 = time.time()

    # Calcul du temps écoulé
    elapsed_time1 = end_time1 - start_time1
    print(f"Le code a pris {elapsed_time1:.5f} secondes à s'exécuter.")

    return 0

if __name__ == '__main__':
    main()