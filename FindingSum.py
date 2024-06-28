nums = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter target: "))
a = len(nums)
for x in range(a):
    for y in range(x+1, a):
        if (nums[x]+nums[y]) == target:
            print ([x,y])
else: print("Not found :(")
