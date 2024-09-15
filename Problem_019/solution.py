import sys
import time

def date():
    day=365%7
    months={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    count=0
    for year in range(1901,2001):
        print(day)
        if year%400==0 or year%4==0:
            leap=1
        elif year%100==0 and year%400!=0:
            leap=0
        else:
            leap=0
        for month in range(1,13):
            if month==2:
                if leap==1:
                    months[2]=29
                else:
                    months[2]=28
            day=(day+months[month])%7
            if day==6:
                count+=1
    return(count)
         



def main():

    start_time1 = time.time()
    print(date())
    end_time1 = time.time()


    elapsed_time1 = end_time1 - start_time1
    print(f"Le code naif a pris {elapsed_time1:.5f} secondes à s'exécuter.")

    return(0)

if __name__ == '__main__':
    sys.exit(main())