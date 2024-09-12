import sys

def main():
    a=1
    b=2
    sum=0
    while b<4000000:
        if b%2==0:
            sum+=b
        temp=b
        b=a+b
        a=temp
    print(sum)
    return(0)

if __name__ == '__main__':
    sys.exit(main())