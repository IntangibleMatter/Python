#numbers array
nums = [5,4,3,2,1]

maxn = -1

for i in nums:
    for j in nums:
        if j - i > maxn:
            maxn = j - i
        nums.pop(0)

print(maxn)
            
