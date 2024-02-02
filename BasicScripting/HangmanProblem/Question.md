# Hangman Problem

Hangman is a classic word-guessing game where one player thinks of a word and the other player tries to guess it by suggesting letters. The word to be guessed is represented by dashes, each dash indicating a letter in the word. As the player guesses correctly, the corresponding dashes are replaced with the correct letters. However, the player has a limited number of incorrect guesses before the game ends.

## Your Task

Write a Python program to implement the Hangman game. Your program should include the following functionalities:

1. Choose a random word from a predefined list of words.
2. Display the current state of the word with dashes for unrevealed letters.
3. Allow the player to guess letters.
4. Update the display with correct guesses.
5. Keep track of incorrect guesses and limit the total allowed incorrect guesses.
6. End the game when the word is guessed correctly or when the allowed incorrect guesses are exhausted.

### Example

For example, if the word is "hangman" and the player guesses "a", the display could look like this:

``` python
Word: _ _ _ _ a _ _
Incorrect guesses: 1
```

### Constraints

- Use a list of predefined words for simplicity.
- You can choose a fixed number of incorrect guesses before the game ends.

Feel free to add comments in your code to explain the logic.

Good luck!
