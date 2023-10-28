#To build a basic quiz game 
# It should contain a lot of question 
# take user input and evaluate the answer 
# mark the score 

import random

quiz_ques = [
    {
        "ques": "What is the capital of France?",
        "choices": ["A) London", "B) Berlin", "C) Paris", "D) Tokyo"],
        "Correct_ans": "C",
    },
 {
        "ques": "What is the capital of Japan?",
        "choices": ["A) London", "B) Berlin", "C) Paris", "D) Tokyo"],
        "Correct_ans": "D",
    },
 {
        "ques": "What is the capital of Germany?",
        "choices": ["A) London", "B) Berlin", "C) Paris", "D) Tokyo"],
        "Correct_ans": "B",
    },
    {
        "ques": "What is the capital of UK?",
        "choices": ["A) London", "B) Berlin", "C) Paris", "D) Tokyo"],
        "Correct_ans": "A",
    },
    {
        "ques": "What is the longest river in the world?",
        "choices": ["A) Great Ganga", "B) Amazon", "C) Nile", "D) Niger"],
        "Correct_ans": "C",
    },
   {
        "ques": "What is the largest ocean in the world?",
        "choices": ["A) Indian Ocean", "B) Pacific Ocean", "C) Atlantic Ocean", "D) Artic Ocean"],
        "Correct_ans": "B",
    },
    {
        "ques": "What is the largest animal in the world?",
        "choices": ["A) Shark", "B) Blue Whale", "C) African Elephant", "D) Giraffe"],
        "Correct_ans": "B",
    },
]

def display_message():
    print('''
--------------------------------------------------------------------------
          Welcome to the quiz game,
          Here are the rules for this game.
          -You are shown four options (A/B/C/D)
          -You have to select one 
          -If your answer is correct then you will be awarded a mark 
          -Else no marks are awarded.
          -Best of luck!
--------------------------------------------------------------------------
          ''')
def ask_ques(question):
    print(question["ques"])
    for choice in question["choices"]:
        print(choice)

def evalutate(user_input, question):
    correct_ans = question["Correct_ans"]
    if user_input == correct_ans:
        print("You got it right!")
        return 1
    else:
        print(f"The correct answer was {correct_ans}")
        return 0
    
def main():
    display_message()
    random.shuffle(quiz_ques)
    score = 0
    for question in quiz_ques:
        ask_ques(question)
        user_in = input("Your answer (A/B/C/D): ").strip().upper()
        score += evalutate(user_in, question)

    print(f"Your final score {score}/{len(quiz_ques)}")
    print("Thank you")

if __name__== "__main__":
    main()