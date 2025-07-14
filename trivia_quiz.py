# France Trivia Quiz

import random

print("How much do you know about France? Let's find out with the quiz below!")

def quiz_generator(questions):
    score = 0
    random.shuffle(questions)

    for question_data in questions:
        question = question_data["question"]
        options_dict = question_data["options"]
        correct_answer = question_data["answer"]

        print("\n" + question)

        # Convert options dictionary to a list of values and shuffle
        options = list(options_dict.values())
        random.shuffle(options)

        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")

        while True:
            try:
                user_answer_index = int(input("Enter your answer (number): ")) - 1
                if 0 <= user_answer_index < len(options):
                    user_answer = options[user_answer_index]
                    break
                else:
                    print("Invalid input. Please enter a number within the range of options.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer was: {correct_answer}\n")

    print(f"You got {score} out of {len(questions)} questions correct.")

questions = [
    {
        'question': "What is the capital of France?",
        'options': {'A': "Berlin", 'B': "Madrid", 'C': "Paris", 'D': "Rome"},
        'answer': "Paris"
    },
    {
        'question': "What is the national flower of France?",
        'options': {'A': "Rose", 'B': "Iris", 'C': "Daffodil", 'D': "Tulip"},
        'answer': "Iris"
    },
    {
        'question': "How many kinds of cheese does France produce?",
        'options': {'A': "1000", 'B': "1200", 'C': "1400", 'D': "1600"},
        'answer': "1600"
    },
    {
        'question': "What is the nickname for the shape of France, referring to its hexagonal form?",
        'options': {'A': "L'Hexagone", 'B': "L'Île-de-France", 'C': "La Riviera", 'D': "La Belle France"},
        'answer': "L'Hexagone"
    },
    {
        'question': "What is the name of the largest river in France?",
        'options': {'A': "The Rhone", 'B': "The Seine", 'C': "The Loire", 'D': "The Rhone"},
        'answer': "The Loire"
    }
]

quiz_generator(questions)
