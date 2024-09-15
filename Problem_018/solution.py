import sys
import time


# INCOMPLET
str="""75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

def convert_matrix(seq):
    list1=seq.split("\n")
    list2=[]
    for i in range(len(list1)):
        list2+=[list1[i].split(" ")]
    for i in range(len(list2)):
        for j in range(i+1):
            list2[i][j]=int(list2[i][j])
    return(list2)

def convert_list(seq):
    list1=seq.split("\n")
    list2=[]
    for i in range(len(list1)):
        list2+=list1[i].split(" ")
    for i in range(len(list2)):
        list2[i]=int(list2[i])
    return(list2)



def valide2(id):
    ligne=(-1+(1+8*id)**(1/2))//2
    col=id-ligne*(ligne+1)//2
    if ligne==col:
        return(id+ligne+1,id+ligne+1+1,id-ligne-1)
    elif col==0:
        return(id+ligne+1,id+ligne+1+1,id-ligne+1)
    else:
        return(id+ligne+1,id+ligne+1+1,id-ligne,id-ligne-1-1)
    
def valide(id):
    ligne=int((-1+(1+8*id)**(1/2))//2)
    return(id+ligne+1,id+ligne+1+1)

    
def solution(list):
    foret=["Null",list[0]]
    n=len(foret)
    count=0
    while len(foret)<2**15:
        for i in range(2**count,n):
            foret.append(list[valide(count)[0]]+foret[i])
            foret.append(list[valide(count)[1]]+foret[i])
        n=len(foret)
        count+=1
        print(foret)
    print(len(foret))
    print(len(list))
    print(max(foret[-16385:-1]))

            
            
def somme():
    somme=0
    for i in range(1,15):
        somme+=2**i     

    return(somme)   
         



def main():

    start_time1 = time.time()

    #On convertit le texte en tableau triangulaire inferieure.
    list=convert_list(str)
    print("Voici la liste de tous les entiers")
    print(list)
    
    print(solution(list))

    print(somme())
    end_time1 = time.time()


    elapsed_time1 = end_time1 - start_time1
    print(f"Le code naif a pris {elapsed_time1:.5f} secondes à s'exécuter.")

    return(0)

if __name__ == '__main__':
    sys.exit(main())