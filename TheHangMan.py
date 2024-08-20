from titles import random_words, famous_movies
from hangmanascii import HANGMANPICS
import random

def main():
    title = choose_word(famous_movies)
    # print(title)
    
    # show_board(title)
    
    guess_letter(title)
    

# Function to choose a random title
def choose_word(words):
    return random.choice(words)

#function to guess the letters

def guess_letter(word):
    title = word
    # conver everything to lower case
    word = word.lower()
    
    #Establish initial parameters for the loops
    x = len(HANGMANPICS) - 1
    y = 0
    result = []
    words = []
    
    #run through every letter of the word to convert it into a list
    for i in word:
        #check that the input is a letter
        if i.isalpha() == True:
            
            words.append(i)
            result.append("__")
        elif i == "'":
            words.append(i)
            result.append(i)
        else:
            words.append(" ")
            result.append(" ")
    # Loop for lives and hanging man drawing
    while x > 0:
        print(HANGMANPICS[y])
        # Print current unrevealed letters
        print(" ".join(result) + "\n")
        
        
        # Ask for input
        
        j = input("Please insert letter: ").lower()
        
        # Check that it's one letter
        if len(j) == 1 and j.isalpha() == True:
            
        # Loop to check if the letter is in the word and then input into result list
            if j in word:
                
                if j in result:
                    print("Try another letter")
                
                else:     
                    
                    #Run through every letter in word
                    for k in word:
                        #Check if j equals k
                        if j == k:
                            # loop from 0 to len of words
                            for itr in range(len(words)):
                                if(words[itr] == j): # if the index of the word is equal to the letter j
                                    result[itr] = j # then the same index value is going to occupy the same position in result list
                        
            else:
                
                #This section substracts one life but also draws another part of the hangman
                x -= 1
                y += 1
            
            
            
            
            # print(words)
            #This will finish and close up the came
            if x == 0:
                print(HANGMANPICS[y])
                print("Game Over")
                print(f"Answer: {title}")
                break
            elif result == words:
                print(HANGMANPICS[y])
                print(title)
                print("You won!")
                break
        
        # If the input is not a single letter, it will ask for input again
        else:
            print("Try One Letter!")
        
            

main()