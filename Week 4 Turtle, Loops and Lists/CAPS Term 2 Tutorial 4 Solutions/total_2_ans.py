nums = [3, 6, 9, 12]
print('The current list is %s' % nums)
new_num = int(input('Please add a new number to the list: '))
nums.append(new_num)

total = 0
# for each number (item) in nums
for n in nums:
    total += n

print('The total is %d' % total)
