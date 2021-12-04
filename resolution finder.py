sf = []
s = []
e = []
for i in range(1,256):
    x = i * 16
    y = i * 9

    if x % 64 == 0 and y % 64 == 0:
        print("%s x %s <------------- 64!"%(x,y))
        sf.append("%s x %s"%(x,y))
    elif x % 16 == 0 and y % 16 == 0:
        print("%s x %s <--------- 16!"%(x,y))
        s.append("%s x %s"%(x,y))
    elif x % 8 == 0 and y % 8 == 0:
        print("%s x %s <--------- 8!"%(x,y))
        e.append("%s x %s"%(x,y))
    else:
        print("%s x %s"%(x,y))

print("64: " + str(sf))
print("16: " + str(s))
print("8: " + str(e))

input("press enter to finish")
