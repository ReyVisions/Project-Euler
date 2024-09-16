import time
import math

def main():
    start_time1 = time.time()

    list=[]
    for i in range(9,-1,-1):
        list.append(math.factorial(i))
    print(list)

    numbers_left=999999
    i=0
    number=0
    numbers=[0,1,2,3,4,5,6,7,8,9]
    seq=""
    while numbers_left>0: 
        print(numbers_left)
        if numbers_left-list[i]>=0:
            number+=1
            numbers_left-=list[i]
        if numbers_left-list[i]<0:
            i+=1
            seq+=str(number)
            number=0
    while len(seq)<10:
        seq+="0"
    
    seq_finale=""
    left=[0,1,2,3,4,5,6,7,8,9]
    for i in range(len(seq)):
        seq_finale+=str(left[int(seq[i])])
        left.pop(int(seq[i]))
        print(left,int(seq[i]))
    

    print(int(seq_finale))


            
            
        


    end_time1 = time.time()

    # Calcul du temps écoulé
    elapsed_time1 = end_time1 - start_time1
    print(f"Le code a pris {elapsed_time1:.5f} secondes à s'exécuter.")

    return 0

if __name__ == '__main__':
    main()