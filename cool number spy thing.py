from random import randint
from time import sleep

i = 0
j = 0
k = 0
l = 0
m = 0
n = 0

while True:
    i = randint(0,255)
    j = randint(0,255)
    k = randint(0,255)
    l = randint(0,255)
    m = randint(0,255)
    n = randint(0,255)
    print(str(i) + "." + str(j) + "." + str(k) + "." + str(l) + "." + str(m) + "." + str(n))
    sleep(0.1)
