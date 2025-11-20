#MW_CP1 Mapping practice

#list of nums
nums = [3, 7, 12, 25, 30, 45, 50, 65, 70, 85, 90, 105, 110, 125, 130, 145, 150, 165, 170, 185, 190, 205, 210, 225, 230, 245, 250, 265, 270, 285]
#sqrd = list(map(lambda og: (og**2), nums))
sqrd = list(map(lambda og: og**2, nums))
#for I, num in enumerate nums:
for i, num in enumerate(nums):
    #print "original number: {num}, squared number: {sqrd[i]}"
    print(f"original number: {num}, squared number: {sqrd[i]}")