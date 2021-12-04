nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

i = 0

for num in nums:
    for n in nums:
        print(num + n + " = "  + str(i))
        i += 1
