from gibberish import Gibberish
from random import randint 

gib = Gibberish()

#random 1 - 4 1 = both false, 2 = start true, 3 = false true, 4 = both false 

program = True
while program:
    numWords = randint(1,1)
    if numWords == 1: #If only 1 word will be generated
        gibVowel = randint(1,3)
        if gibVowel == 1:
            print(f"\n{gib.generate_word()}")

        elif gibVowel == 2: #prints 1 word that starts with a vowel
            print(f"\n{gib.generate_word(start_vowel=True)}")

        elif gibVowel == 3: #prints 1 word that ends with a vowel
            print(f"\n{gib.generate_word(end_vowel= True)}")
        
            
        continueChoice = int(input("\nWould you like to generate another name for a system? Enter a 1 for yes or a 2 for no: ")) #checks to see if the user wants to generate another system name
        if continueChoice == 1:
            program = True
            
        elif continueChoice == 2:
            program = False