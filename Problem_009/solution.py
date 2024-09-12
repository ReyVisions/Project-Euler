import sys

def problem9():
    for a in range(1,999):
        for b in range(a,1000):
            c=1000-a-b

            if a*a+b*b==c*c and c>0:
                print(a)
                print(b)
                print(c)
                return(a*b*c)

def main():
    print(problem9())
    return(0)

if __name__ == '__main__':
    sys.exit(main())