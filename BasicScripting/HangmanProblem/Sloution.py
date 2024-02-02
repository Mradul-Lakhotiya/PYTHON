import random
import HangmanArt
import HangmanWord

chosen_word = random.choice(HangmanWord.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(HangmanArt.logo)

print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

guessed = []
    
while not end_of_game:
    guess = input("Guess a letter: ")[0].lower()

    if guess in guessed:
        print(f"The Letter {guess} is already Guessed")
    else:
        #Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        #Check if user is wrong.
        if guess not in chosen_word:
            
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")

        #Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        #Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")
            
        print(HangmanArt.stages[lives])