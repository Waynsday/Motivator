import random
import os
import time

def counting(x):
    total = 0
    for l in x:
        total += 1
    x.seek(0)
    return total


def genline(x):
    a = random.randint(1, counting(x))
    count = 0
    for l in x:
        count += 1
        if count == a:
            return l


#start of main program

fh = open('phrases.txt', 'r+')
clear = lambda: os.system('clear')
#Main menu
while True:
    print("Input the number of your selected option: ")
    print("1. Receive Insult")
    print("2. Add Insult")
    print("3. Close program")
    while True:
        entry = input("Enter option: ")
        try:
            ans = int(entry)
            break
        except:
            print("Invalid input")

    if ans is 1:
        print(genline(fh))
        time.sleep(5)
    elif ans is 2:
        new = input("Enter new insult: ")
        fh.seek(0, 2)
        fh.write("\n")
        fh.write(new)
        print("Successfully added!")
        time.sleep(3)
    elif ans is 3:
        fh.close()
        print("Thank you for using this program!")
        time.sleep(3)
        break
    else:
        print("Invalid Input")

    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n')




