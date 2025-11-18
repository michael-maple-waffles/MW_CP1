#MW_CP1 Flexibal calculator

#funtion one GROUP(*nums, prod_sum)
def group(*nums, prod_sum):
    #if prod_sum == "sum"
    if prod_sum == "sum":
        #total += (num for num in nums)
        total += (num for num in nums)
    #elif prod_sum == "prod"
    elif prod_sum == "prod":
        #total *= (num for num in nums)
        total *= (num for num in nums)
    #return total
    return total

#function for AVERAGE(*nums)
def average(*nums):
    adding += (num for num in nums)
    #adding divided by length of nums = complete
    complete = adding/len(nums)
    #return complete
    return complete

#function for max/min(*nums, choice)
def maxMin(*nums, choice):
    #if choice == "max"
    if choice == "max":
        #return max(nums)
        return max(nums)
    #elif choice == "min"
    elif choice == "min":
        #return min(nums)
        return min(nums)

#while True
while True:
    #ask what they would like to do
    pick = input("This program can do 5 different calculations, you can do sum, product, average, max, and min\n\n Press 1 for sum, Press 2 for product, Press 3 for average, Press 4 for max, and Press 5 for min. If you are done press 6")
    #ask for nums
    get_nums = []
    while True:
        getting_num = input("what is your num? Type 'done' if you are done").strip().lower()
        if getting_num == 'done':
            break
        else:
            get_nums += float(getting_num)

    
    



