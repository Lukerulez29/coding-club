  
done = 0
nums = []

while done != 1:
    print("Type in a number you want to choose and press enter to select the next one.")
    nums.append(int(input()))
    print("Are you done? If so, press 1. Otherwise, press any number and enter.")
    done = int(input())
print("Select a target number.")
target = int(input())

i = 0
while i < len(nums):
    if target - nums[i] in nums[i+1:]:
        a = target - nums[i]
        a = nums.index(a, i+1, len(nums))
        print(nums)
        print(i, a)
    i+=1