#MW_CP1 Ceaser Cypher

#function RESETTER to ensuring that the ceaser cypher doesnt print something that isnt a letter Parameters are MAX and MIN and SHIFTER and LETTER
def resetter(max, min, shifter, letter):
    #modulo shifter by 26
    shifting = ord(letter)
    shifter = shifter % 26
    while shifter > 0:
        shifter -= 1
        shifting += 1
        
        if shifting > max:
            shifting = min
    return chr(shifting)


#function RUNNER pertaining to asking the user what they want to input (both for the word and the number to shift)
def runner(doing):
    #get user word
    word = input(f"What is the word you would like to {doing}?").strip()
    for i in word:
        if i in ["`", "~", "!", "@", "#", "$", "%","^","&","*","(", ")", "-","_", "=", "+","[","]","{","}","\\","|", "<",">",",",".",";",":","\"", "'"," ", "?","/"]:
            return "Ensure you are not using any spaces or special characters pls!"
    #get user shift
    shifter = int(input("How much are we shifting by?"))
    #for items in word 
    for letter in word:
        #IF item is upper:
        if letter.isupper():
            # call RESETTER(90,65,SHIFT)
            shifted += resetter(90, 65, shifter, letter)
        #elif item is lower:
        elif letter.islower():
            # call RESETTER(122,97,SHIFT)
            shifted += resetter(122, 97, shifter, letter)
    return shifted

while True:
    choice = input("Press '1' if you would like to encode a message, press '2' if you would like to decypher a message, press '3' if you would like to be done.")
    if choice == 1:
        runner("encode")