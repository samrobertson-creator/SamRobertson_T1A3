# SamRobertson_T1A3

## Source Code Repository

[https://github.com/samrobertson-creator/SamRobertson_T1A3]

## Python Quiz Application

A basic quiz that tests your knowledge of random facts, and challenges the user to score 100%, and take home the gran prize of $1,000,000!

## Running Program

To launch this program, open your termianl or command line. After that type "python3" and them drag the file app.py into the terminal. After that hit enter and the application will be ran in terminal

## Features

### Feature 1: Interactive

The program begins by providing help to the user with a brief explanation of how the program works and how to use it. Then the user is prompted to enter their name, which is stored as a variable under 'name' and is later used throughout the program.

### Feature 2: Questions

After the user enters their name, they are then asked their first question. Each question has 4 potential answers assigned to them, using a nested for loop and indexing each question number. They will read the question, and read the possible answers that are assigned to a given letter (either A, B, C or D). The program than checks your guess against the correct answer. If the user's guess matches the correct answer, they are told they are correct and the program takes them to the next question.

### Feature 3: Results

As previously mentioned, the user is either scored correct or wrong after each question. If their guess matches the answer, the 'correct guesses' variable is then appended and given a +1. Once the user has finished all the questions, all the correct answers are displayed and underneath them are the user's guesses. This was done by using another for loop which retirievd the both the array index of the user's guesses and the correct answers.

## Implementation

Each of the key features were implemetned via the main programming concepts and structures required for this projects. Although it was briefly spoken about during the features it would be best to reiterate. Variables were used to store data such as the users name and their guesses. A while loop was utulised with the play_again feature, and nested for loops were used to match the correct question index with the correct options. Error handling was used mainly with the '.upper' function, no errors were found outside of that so 'try' and 'except' error handling methods were not necessary. Python imports were used for the help package. Finally, basic user input and output was used.

## Error Handling

No instances errors were found in the final program. In situations where the user is required to input, the function .upper was utilised to avoid any capitilation mistakes. Although the user is prompted to enter either a, b, c or d with each question, the user may input any answer and it will not print an error. This is because a dictionary is utlisied for the questions in the game, so each question has an answer key linked to it. However they will obvious get the question wrong if it is not equal to the answer key provided in the question dictionary.