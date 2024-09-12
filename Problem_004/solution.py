import sys

def palindrome():
    max=0
    for i in range(1000):
        for j in range(1000):
            if str(i*j)==str(i*j)[::-1]:
                if max<i*j:
                    max=i*j
    return(max)

def main():
    print(palindrome())
    return(0)

if __name__ == '__main__':
    sys.exit(main())