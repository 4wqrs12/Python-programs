nums = [2,7,11,15]

target = 9
working = {""}

for num in range(len(nums)):
    for num2 in range(len(nums)):
        if nums[num] + nums[num2] == target and num != num2:
            working.add(num)
            working.add(num2)

working.remove("")
working_list = list(working)
print(f"Indices: {working_list}")
