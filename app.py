# -------------------------
import help
print(help)


name = input("Hi there, welcome to Hotseat Millionaire, what is your name? ")
print("Okay " + name + ", here is your first Question:")

def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%!")

# -------------------------
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------


questions = {
 "Who created Python?: ": "A",
 "What year was Python created?: ": "B",
 "Which is the only part of the body that cannot heal itself?": "A",
 "It is illegal to own which of the following animals in Switzerland?: ": "C",
 "Which is the only planet that spins clockwise?:": "D",
 "Which of the following letters doesn't appear in any of the U.S.A. states?": "B",
 "The largest internal organ in the human body is the what?": "A",
 "Which is the only animal capable of clapping to a musical beat?": "D",
 "What did the Famous Hollywood sign say before it was changed in 1949?": "B",
 "What percentage of American Adults believe chocolate milk originates from brown cows?": 'D'
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Teeth", "B. Ears", "C. Tongue", "D. Eyes"],
          ["A. Cat", "B. Mouse", "C. Guinea Pig", "D. Possum"],
          ["A. Jupiter", "B. Mars", "C. Earth", "D. Venus"],
          ["A. Z", "B. Q", "C. X", "D. V"],
          ["A. Small intestine", "B. Large intestine", "C. Stomach", "D. Lungs"],
          ["A. Dolphin", "B. Otter", "C. Monkey", "D. Sea Lion"],
          ["A. Hollwoodville", "B. Hollywoodland", "C. Hollywoodtown", "D. Hollywoodhills"],
          ["A. 2%", "B. 13%", "C. 7%", "D. 22%"]]


new_game()

while play_again():
    new_game()

print("Okay thanks for playing " + name + ", see you next time :)")