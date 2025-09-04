#MW_CP1 madlib practice

#user inputs var

user_inputs = {

}

user_inputs["name"] = input("Give me the name! ")
user_inputs["pronoun_regular"] = input("Give me a pronoun (regular)! ")
user_inputs["pronoun_possessive"] = input("Give me a pronoun (possesive)! ")
user_inputs["age"] = input("Give me a number! ")
user_inputs["cookable"] = input("Give me a singular cookable item! ")
user_inputs["actions"] = input("Give me a verb ending in ing! ")
user_inputs["day_describer"] = input("What is the day like? ")


story = "\n" + user_inputs["name"] + " was making a " + user_inputs["cookable"] + ". " + user_inputs["pronoun_regular"] + " has always enjoyed a good " + user_inputs["cookable"] + " on a " + user_inputs["day_describer"] + " day. Luckily " + user_inputs["name"] + " has always felt that times like this were perfect for turtle " + user_inputs["actions"] + ". Although many people found their morning activities extroardinarily peculiar " + user_inputs["name"] + " still enjoyed every second of it. For they had lived " + user_inputs["age"] + " years, enough to give the maturity to understand how important doing the tasks you love is."

print(story)
