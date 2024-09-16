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
    list_NA=[]
    for i in range(len(abondants)):
        for j in range(len(abondants)):
            list_NA.append(abondants[i]+abondants[j])
    for i in range(28123):
        if i not in list_NA:
            sum_non_abondants+=i
    print(sum_non_abondants)


    end_time1 = time.time()

    # Calcul du temps écoulé
    elapsed_time1 = end_time1 - start_time1
    print(f"Le code a pris {elapsed_time1:.5f} secondes à s'exécuter.")

    return 0

if __name__ == '__main__':
    main()