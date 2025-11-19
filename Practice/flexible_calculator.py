#MW_CP1 Flexibal calculator


import math
#funtion one GROUP(*nums, prod_sum)
def group(*nums):
    #if prod_sum == "sum"
    if nums[1] == "sum":
        #total += (num for num in nums)
        total = sum(nums[0])
    #elif prod_sum == "prod"
    elif nums[1] == "prod":
        #total *= (num for num in nums)
        total = math.prod(nums[0])
    #return total
    return total

#function for AVERAGE(*nums)
def average(*nums):
    adding = sum(nums[0])
    #adding divided by length of nums = complete
    complete = adding/len(nums)
    #return complete
    return complete

#function for max/min(*nums, choice)
def maxMin(*nums):
    #if choice == "max"
    if nums[1] == "max":
        #return max(nums)
        return max(nums[0])
    #elif choice == "min"
    elif nums[1] == "min":
        #return min(nums)
        return min(nums[0])

#while True
while True:
    #ask what they would like to do
    pick = input("This program can do 5 different calculations, you can do sum, product, average, max, and min\n\n Press 1 for sum, Press 2 for product, Press 3 for average, Press 4 for max, and Press 5 for min. If you are done press 6:  ")
    #ask for nums
    get_nums = []
    while True:
        getting_num = input("what is your num? Type 'done' if you are done:  ").strip().lower()
        if getting_num == 'done':
            break
        else:
            get_nums.append(float(getting_num))

    if pick == '1':
        print(f"\nThe sum of your numbers is: {group(get_nums, "sum")}\n")
    elif pick == '2':
        print(f"\nthe product of your numbers is: {group(get_nums, "prod")}\n")
    elif pick == '3':
        print(f"\nThe average of your numbers is: {average(get_nums)}\n")
    elif pick == '4':
        print(f"\n The maximum of your numbers is: {maxMin(get_nums, "max")}\n")
    elif pick == '5':
        print(f"\n The minimum of your numbers is: {maxMin(get_nums, "min")}\n")
    elif pick == '6':
        print("goodnight")
        break
    
    



