print("Factor Finder")

factors = []
def find_factors(num):
    for i in range(0,num):
        if num%i == 0:
            factors.append(i)