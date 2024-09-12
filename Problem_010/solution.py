import sys

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
    print(problem10())
    return(0)

if __name__ == '__main__':
    sys.exit(main())