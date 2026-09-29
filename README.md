# Quiz / Trivia Game

A command-line quiz game built with Python.

This project was created as part of my Python project-based learning journey. It helped me practice functions, lists, dictionaries, loops, input validation, randomization, score calculation, and program structure.

## Features

* Multiple-choice trivia questions
* Four answer options per question
* Answer validation
* Random selection of questions
* Randomized answer options
* Score tracking
* Percentage calculation
* Replay option
* Handles invalid user input

## How the Game Works

When the game starts, the user chooses how many questions they want to answer.

The program then:

1. Selects random questions from the question bank.
2. Shuffles the answer options.
3. Displays each question.
4. Accepts the user's answer.
5. Checks whether the selected answer is correct.
6. Updates the score.
7. Calculates the final percentage.
8. Asks whether the user wants to play again.

## Example

```text
What is the capital of Nigeria?

A. Lagos
B. Kano
C. Abuja
D. Ibadan

Your answer: C

Correct!
```

## Technologies Used

* Python 3
* `random` module
* Lists
* Dictionaries
* Functions
* Loops
* Conditional statements
* Exception handling

## Project Structure

```text
quiz-game/
│
├── quiz.py
└── README.md
```

## How to Run

1. Clone the repository:

```bash
git clone <github.com/MubarakAdesola1>
```

2. Navigate into the project:

```bash
cd quiz-game
```

3. Run the program:

```bash
python3 quiz.py
```

## Main Functions

### `ask_question()`

Handles one question by:

* Displaying the question
* Displaying the options
* Getting the user's answer
* Validating the input
* Checking the answer
* Returning `True` or `False`

### `play_game()`

Handles one complete game by:

* Selecting random questions
* Shuffling the options
* Calling `ask_question()`
* Tracking the score
* Calculating the percentage

### `main()`

Controls the overall program flow, including:

* Asking how many questions to play
* Starting the game
* Asking whether to play again
* Ending the program

## What I Learned

Through this project, I practiced:

* Creating reusable functions
* Passing arguments to functions
* Returning values from functions
* Working with dictionaries and lists
* Using `enumerate()`
* Validating user input
* Using `try` and `except`
* Using `break` and `continue`
* Using `random.sample()`
* Using `random.shuffle()`
* Tracking scores
* Calculating percentages
* Organizing a program into separate responsibilities
* Understanding how functions can call other functions

## Future Improvements

Possible improvements include:

* Add different quiz categories
* Add difficulty levels
* Add a timer
* Add a high-score system
* Load questions from a JSON file
* Add more questions
* Add more detailed results

## Status

Completed ✅

This project is part of my Python learning journey.
# trivia-game
