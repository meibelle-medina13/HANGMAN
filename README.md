# Hangman Game (Tkinter)

A simple Hangman game built with Python's Tkinter library. Guess the word one letter at a time before the stickman is fully drawn!

## Requirements
- Python 3.9.7

## Features
- GUI made with Tkinter
- Every wrong guesses, hangman picture will be displayed at a time
- Different categories to choose from
- Each category has 10 levels
- A background music and sound effects that adds enjoyment to the game

## How to Run
1. Clone the repository
    ```bash
    git clone https://github.com/meibelle-medina13/HANGMAN.git
    ```
2. Proceed to cloned repository path
    ```bash
    cd HANGMAN
    ```
3. Run the game
    ```bash
    python main.py
    ```

## How it Works?
- A word in each level is selected from a word list
- Users will use on-screen buttons to guess a letter
- Each wrong guess displays a part of a hangman
- When the user guess the word, it will unlock the next level, otherwise, user may replay the level