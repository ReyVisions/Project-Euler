import sys

def main():
    divisors=0
    n=1
    max=1
    while divisors<500:
        divisors=0
        max=n*(n+1)//2

        for i in range(1,2+int(max**(1/2))):
            if max%i==0:
                divisors+=2
        n+=1
    print(max)
    return(0)

if __name__ == '__main__':
    sys.exit(main())