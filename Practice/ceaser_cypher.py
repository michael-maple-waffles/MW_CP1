#MW_CP1 Ceaser Cypher

#function RESETTER to ensuring that the ceaser cypher doesnt print something that isnt a letter Parameters are MAX and MIN and SHIFTER and LETTER
def resetter(max, min, shifter, letter, doing):
    #modulo shifter by 26
    shifting = ord(letter)
    shifter = shifter % 26
    if doing == "encode":
        while shifter > 0:
            shifter -= 1
            shifting += 1
            
            if shifting > max:
                shifting = min

    elif doing == "decypher":
         while shifter > 0:
            shifter -= 1
            shifting -= 1
            
            if shifting < min:
                shifting = max

    return chr(shifting)


#function RUNNER pertaining to asking the user what they want to input (both for the word and the number to shift)
def runner(doing):
    shifted = ""
    #get user word
    word = input(f"What is the word you would like to {doing}?(do not use special characters or numbers) ").strip()
    for i in word:
        if i in ["`", "~", "!", "@", "#", "$", "%","^","&","*","(", ")", "-","_", "=", "+","[","]","{","}","\\","|", "<",">",",",".",";",":","\"", "'"," ", "?","/"] or i.isdigit():
            return "Ensure you are not using any spaces or special characters pls!"
        
    if doing == "encode":
    #get user shift
        shifter = int(input("How much are we shifting by ?(insert a number) ").strip())
        #for items in word 
        for letter in word:
            #IF item is upper:
            if letter.isupper():
                # call RESETTER(90,65,SHIFT)
                shifted += (resetter(90, 65, shifter, letter, doing))
            #elif item is lower:
            elif letter.islower():
                # call RESETTER(122,97,SHIFT)
                shifted += (resetter(122, 97, shifter, letter, doing))
        return f"your encrypted message is {shifted}"

    elif doing == "decypher":
        shifter = int(input("How much was this shifted by?(insert a number) ").strip())
        #for items in word 
        for letter in word:
            #IF item is upper:
            if letter.isupper():
                # call RESETTER(90,65,SHIFT)
                shifted += (resetter(90, 65, shifter, letter, doing))
            #elif item is lower:
            elif letter.islower():
                # call RESETTER(122,97,SHIFT)
                shifted += (resetter(122, 97, shifter, letter, doing))
        return f"\n Your Decyphered word is: {shifted}\n"

print("you will be making a ceasar cypher, dont know what that is? look it up!")

while True:
    choice = input("\n\nPress '1' if you would like to encode a message, press '2' if you would like to decypher a message, press '3' if you would like to be done. ").strip()
    if choice == "1":
        print(runner("encode"))
    elif choice == "2":
        print(runner("decypher"))
    elif choice == "3":
        print("GoodBye!")
        break
    else: 
        print("make sure you are pressing '1' '2' or '3'.\n")
        continue