import sys
import time

dictionnary={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety",100:"hundred"}

def nb_letters(n):
    seq=""
    if n==1000:
        seq="onethousand"
        return(len(seq))
    if n>=100:
        hundreds=n//100
        seq+=dictionnary[hundreds]
        seq+=dictionnary[100]
        if n%100==0:
            return(len(seq))
        else:
            seq+="and"
    n%=100
    if n >= 20:
        tens = n // 10 * 10
        seq += dictionnary[tens]
        n %= 10

    if n!=0:
        seq+=dictionnary[n]
    # Déboguer : Imprimer la chaîne générée pour chaque nombre
    print(f"Nombre: {n}, Chaîne générée: {seq}, Longueur: {len(seq)}")
    return(len(seq))
    


    

def main():
    # Commencer la mesure de temps
    start_time1 = time.time()

    sum=0
    for i in range(1,1001):
        sum+=nb_letters(i)
    print(sum)

    # Fin de la mesure de temps
    end_time1 = time.time()

    # Calcul du temps écoulé
    elapsed_time1 = end_time1 - start_time1
    print(f"Le code naif a pris {elapsed_time1:.5f} secondes à s'exécuter.")

    return(0)

if __name__ == '__main__':
    sys.exit(main())