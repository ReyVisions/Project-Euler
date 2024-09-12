import sys

def factor(entier):
    for i in range(2,int(entier**(1/2))+1):
        if entier==1:
            return(i-1)
        if entier/i==entier//i:
            entier=entier/i
    return(0)

def main():
    print(factor(600851475143))
    return(0)

if __name__ == '__main__':
    sys.exit(main())