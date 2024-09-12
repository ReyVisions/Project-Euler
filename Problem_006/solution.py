import sys

def sum_square_difference():
    a=(100*101)/2
    a=a*a
    b=0
    for i in range(101):
        b+=i**2
    return(a-b)

def main():
    print(sum_square_difference())
    return(0)

if __name__ == '__main__':
    sys.exit(main())