import sys

def smallest():
    i = 1
    for k in (range(1, 21)):
        if i % k > 0:
            for j in range(1, 21):
                if (i*j) % k == 0:
                    i *= j
                    break
    return i  

def main():
    print(smallest())
    return(0)

if __name__ == '__main__':
    sys.exit(main())