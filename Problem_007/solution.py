import sys

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

def main():
    print(problem7())
    return(0)

if __name__ == '__main__':
    sys.exit(main())