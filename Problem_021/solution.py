import sys

def main():
    sumAllAmicable = 0

    naturalList = list(range(2, 10000))

    for number in  naturalList:
        i = 1
        j = 1
        sumDivisors1 = 0
        sumDivisors2 = 0
        while (i < number):
            if number%i == 0:
                sumDivisors1+=i
            i+= 1
        

        while (j < sumDivisors1):
            if sumDivisors1%j == 0:
                sumDivisors2+=j
            j+= 1
 
        if (sumDivisors2 == number and sumDivisors1!=number):
            sumAllAmicable = sumAllAmicable + number + sumDivisors1
            naturalList.remove(number)
            naturalList.remove(sumDivisors1)
    print(sumAllAmicable)
    return 0


if __name__ == '__main__':
    sys.exit(main())