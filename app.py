from Questions import Question

question_prompts = [
    "How many hours are in a day?(a) 24(b) 25",
    "How many hours are in a day?(a) 24(b) 25"
]

questions = [
    Question(question_prompts[0], "a" ),
    Question(question_prompts[1], "a" )
]

def run_quiz(questions):
    score = 0
    for questions in questions:
        answer = input(question_prompts)
        if answer == questions.answer:
            score += 1
    print("You got " + str(score) + " / " + "2 " + "correct")

run_quiz(questions)