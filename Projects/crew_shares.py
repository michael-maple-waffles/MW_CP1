#MW_CP1

#variables
crew_size = 0

money_earned = 0.00

Shares = 0.00

captian_earnings = 0.00

firstmate_earnings = 0.00

crew_earnings = 0.00

#inputs

money_earned = float(input("How much money was earned by the crew?\n"))

crew_size = int(input("How many members of the crew are there? (not including captain and first mate) \n"))

shares = float((money_earned-(500*crew_size)) / (crew_size + 10))

captian_earnings = shares*7

firstmate_earnings = shares*3

print(f"Your captain gets ${captian_earnings:.2f}\n\n Your first mate gets ${firstmate_earnings:.2f} \n\n Your crew still needs ${shares:.2f}")


