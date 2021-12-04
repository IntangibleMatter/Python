#fizzbuzz
version = input("Which version do you want to run? ")

ver = int(version)

def fizz1():
    i = 1
    three = False
    five = False
    string = ""
    while i <= 100:
        string = ""
        three = i % 3 == 0; five = i % 5 == 0;
        if three:
            string += "Fizz"
        if five:
            string += "Buzz"
        if string == "":
            string = str(i)
        print(string)
        i += 1




if ver == 1:
    fizz1()