import random
from hangman_art import logo,stages
from hangman_words import word_list

print(logo)
# Choosing Random Word.
word = word_list[random.randint(0,len(word_list)-1)]
# print(word)

# Displaying Blanks
placeholder=""
for position in word:
    placeholder+="_"
print("Words to Guess --> ",placeholder,"\n")

game_over=False
correct_letters=[]
lives=6
while game_over==False:
    print(f"\n```````````````````````````````````` {lives}/6 LEFT `````````````````````````````````````")
    # Guessing Letter.
    display = ""
    guess = input("Guess a Letter --> ").lower()

    # Already Guessed
    if guess in correct_letters:
        print("\n\t``````````````````````````````````\n\tYou have already guessed this Letter!\n\t``````````````````````````````````\n")

    # Guess in word or not. 
    if len(guess)==1:
        for letter in word:
            if letter == guess: 
                display+=letter
                correct_letters.append(guess)
            # Maintaining Continuity    
            elif letter in correct_letters:
                display+=letter
            else:
                display+="_"
        print(display,"\n")
         # Stages for Correct and Incorrect       
        if guess not in word:
            if lives==0:
                print("\n\tTHE MAN WAS HANGED! YOU LOST! THE WORD WAS --> ", word,"\n")
                game_over=True
            else:
                lives-=1
                print(stages[lives])
        else:
            print(stages[lives])
    else:
        print("\n\tONLY ONE LETTER WAS TO BE CHOSEN! PLAY AGAIN!\n")
        exit()
    if "_" not in display:
        print("\n\tTHE MAN WAS SAVED! YOU WON!\n")
        game_over=True
