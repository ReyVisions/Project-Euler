import time


#INCOMPLET
coins=[200,100,50,20,10,5,2,1]

def toMoney(list):
    sum=0
    for i in range(len(list)):
        sum+=list[0]*coins[0]
    return(sum)


def main():
    start_time1 = time.time()
    
    combinaisons=0
    for i in range(200,180,-1):
        coins_left=i    
        money_left=200
        indice=0
        list=[0,0,0,0,0,0,0,0]
        while coins[indice]*i>200:
            if indice<7:
                indice+=1
        money_left-=i*coins[indice]
        coins_left-=i
        list[indice]=i
        while money_left>0:
            if coins_left==0:
                coins_left+=1
                money_left+=coins[indice]
                list[indice]-=coins[indice]
            if money_left>coins_left*coins[indice]:
                indice-=1
            if money_left<coins_left*coins[indice]:
                for j in range(7,-1,-1):
                    if list[j]>0:
                        
                        indice=j
                        coins_left+=1
                        money_left+=coins[indice]
                        list[indice]-=coins[indice]
                        break
            elif money_left-coins_left*coins[indice]==0:
                money_left-=coins_left*coins[indice]
                list[indice]+=coins_left
                coins_left-=1
            print(i,list)
            if indice==0:
                indice=7
        if money_left==0:
            print(i,list)
            combinaisons+=1
    print(combinaisons)

            
        
  

    end_time1 = time.time()

    # Calcul du temps écoulé
    elapsed_time1 = end_time1 - start_time1
    print(f"Le code a pris {elapsed_time1:.5f} secondes à s'exécuter.")

    return 0

if __name__ == '__main__':
    main()