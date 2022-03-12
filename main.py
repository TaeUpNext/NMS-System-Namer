from gibberish import Gibberish
from random import randint 

gib = Gibberish()

#random 1 - 4 1 = both false, 2 = start true, 3 = false true, 4 = both false 

program = True
while program:
    numWords = randint(1,3)
    if numWords == 1: #If only 1 word will be generated
        gibVowel = randint(1,3)
        if gibVowel == 1:
            print(f"\n{gib.generate_word()}")

        elif gibVowel == 2: #prints 1 word that starts with a vowel
            print(f"\n{gib.generate_word(start_vowel=True)}")

        elif gibVowel == 3: #prints 1 word that ends with a vowel
            print(f"\n{gib.generate_word(end_vowel= True)}")
    
    #creates 2 words       
    elif numWords == 2:  #creates 2 words
        gibVowel1 = randint(1,3)
        gibVowel2 = randint(1,3)
        if gibVowel1 == 1 and gibVowel2 == 1: #both words do not start or end in a vowel
            words = gib.generate_words(2)
            print("\n", *words)
        
        elif gibVowel1 == 1 and gibVowel2 == 2:# 1st word doesnt star/end in vowel, 2nd word starts with vowel
            word1 = gib.generate_word()
            word2 = gib.generate_word(start_vowel = True)
            print(f"\n {word1} {word2}")
        
        elif gibVowel1 == 1 and gibVowel2 == 3: #1st word doesnt star/end in vowel, 2nd word ends with vowel
            word1 = gib.generate_word()
            word2 = gib.generate_word(end_vowel = True)
            print(f"\n {word1} {word2}")
        
        elif gibVowel1 == 2 and gibVowel2 == 1: #1st word starts with a vowel, 2nd  word doesn't star or end in vowel
            word1 = gib.generate_word(start_vowel = True)
            word2 = gib.generate_word()
            print(f"\n {word1} {word2}")
        
        elif gibVowel1 == 2 and gibVowel2 == 2: #both words start with a vowel
            word1 = gib.generate_word(start_vowel = True)
            word2= gib.generate_word(start_vowel = True)
            print(f"\n {word1} {word2}")
        
        elif gibVowel1 == 2 and gibVowel2 == 3: #1st word starts a vowel and the 2nd word ends in a vowel
            word1 = gib.generate_word(start_vowel = True)
            word2 = gib.generate_word(end_vowel = True)
            print(f"\n {word1} {word2}")
        
        elif gibVowel1 == 3 and gibVowel2 == 1: #1st word ends in a vowel 2nd word doesnt start or end in a vowel
            word1 = gib.generate_word(end_vowel = True)
            word2 = gib.generate_word()
            
            print(f"\n {word1} {word2}")
        
        elif gibVowel1 == 3 and gibVowel2 == 2: #1st word ends in a vowel 2nd word starts in a vowel
            word1 = gib.generate_word(end_vowel = True)
            word2 = gib.generate_word(start_vowel = True)
            print("\n {word1} {word2}")
        
        elif gibVowel1 == 3 and gibVowel2 == 3: #both words end in a vowel
            word1 = gib.generate_word(end_vowel = True)
            word2 = gib.generate_word(end_vowel = True)
            print(f"\n {word1} {word2}")
            
            
        continueChoice = int(input("\nWould you like to generate another name for a system? Enter a 1 for yes or a 2 for no: ")) #checks to see if the user wants to generate another system name
        if continueChoice == 1:
            program = True
            
        elif continueChoice == 2:
            program = False