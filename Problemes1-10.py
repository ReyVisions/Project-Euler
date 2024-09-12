import sys

#First 10 problems

def factor(entier):
    for i in range(2,int(entier**(1/2))+1):
        if entier==1:
            return(i-1)
        if entier/i==entier//i:
            entier=entier/i
    return(0)


def palindrome():
    max=0
    for i in range(1000):
        for j in range(1000):
            if str(i*j)==str(i*j)[::-1]:
                if max<i*j:
                    max=i*j
    return(max)
    
def smallest():
    i = 1
    for k in (range(1, 21)):
        if i % k > 0:
            for j in range(1, 21):
                if (i*j) % k == 0:
                    i *= j
                    break
    return i  

def sum_square_difference():
    a=(100*101)/2
    a=a*a
    b=0
    for i in range(101):
        b+=i**2
    return(a-b)

def problem7():
    list=[]
    n=1
    factors=0
    while len(list)<10001:
        factors=0
        for i in range(2,int(n**(1/2))+2):
            if n%i==0:
                break
            if i==int(n**(1/2))+1:
                list.append(n)
        n+=1
        print(len(list))
    return(list[-1])

def problem8(str):
    max=1
    temp=str[0:13]
    for i in range(13):
        max*=int(temp[i])
    for i in range(len(str)-13):
        sum=1
        temp=str[0+i:13+i]
        for j in range(13):
            sum*=int(temp[j])
        if max<sum:
            max=sum
    return(max)

def problem9():
    for a in range(1,999):
        for b in range(a,1000):
            c=1000-a-b

            if a*a+b*b==c*c and c>0:
                print(a)
                print(b)
                print(c)
                return(a*b*c)

def problem10():
    sum=2
    counter=2
    while counter<2000000:
        for i in range (2,int(counter**(1/2))+2):
            if counter%i==0:
                break
            if i==int(counter**(1/2)+1):
                sum+=counter
        counter+=1
        print(sum)
    return(sum)



def main():
    #print(factor(600851475143))
    #print(palindrome())
    #print(smallest())
    #print(sum_square_difference())
    #print(problem7())
    """print(problem8("73167176531330624919225119674426574742355349194934"
+"96983520312774506326239578318016984801869478851843"
+"85861560789112949495459501737958331952853208805511"
+"12540698747158523863050715693290963295227443043557"
+"66896648950445244523161731856403098711121722383113"
+"62229893423380308135336276614282806444486645238749"
+"30358907296290491560440772390713810515859307960866"
+"70172427121883998797908792274921901699720888093776"
+"65727333001053367881220235421809751254540594752243"
+"52584907711670556013604839586446706324415722155397"
+"53697817977846174064955149290862569321978468622482"
+"83972241375657056057490261407972968652414535100474"
+"82166370484403199890008895243450658541227588666881"
+"16427171479924442928230863465674813919123162824586"
+"17866458359124566529476545682848912883142607690042"
+"24219022671055626321111109370544217506941658960408"
+"07198403850962455444362981230987879927244284909188"
+"84580156166097919133875499200524063689912560717606"
+"05886116467109405077541002256983155200055935729725"
+"71636269561882670428252483600823257530420752963450"))"""
    print(problem9())
    print(problem10())
    return(0)


if __name__ == '__main__':
    sys.exit(main())