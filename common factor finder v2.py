import time
def cff():
    print("Common factor finder")
            
    num1 = input("Input a number: ")
    
    num2 = input("Input another number: ")
    
    num1 = int(num1)
    num2 = int(num2)


    if num1 > 99999 or num2 > 999999:
        print("Calculating, please wait. ")
    i = 1
    
    
    int1 = [ ]
    
    int2 = [ ]
    
    common = [ ]
    t0 = time.time()
    
    while i <= num1 or i <= num2:
        if num1 % i == 0 and num2 % i == 0:
            int1.append(i)
            int2.append(i)
            common.append(i)
        elif num1 % i == 0 or num2 % i == 0:
            if num1 % i == 0:
                int1.append(i)
            if num2 % i == 0:
                int2.append(i)
        i = i + 1
    t1 = time.time()

    total = t1-t0
    print("")
    print("Calculations took " + str(total) + " seconds overall.")
    print("")
    print("Factors of " + str(num1) + ": ")
    print(int1)
    print("")
    print("Factors of " + str(num2) + ": ")
    print(int2)
    print("")
    print("Common factors: ")
    print(common)
    
    time.sleep(1)
    yn = ""
    yn = input("Would you like to find common factors for two more numbers? y/n: ")
    if yn.lower() == "y":
        print("")
        print("")
        print("")
        cff()
    else:
        return 0

cff()
