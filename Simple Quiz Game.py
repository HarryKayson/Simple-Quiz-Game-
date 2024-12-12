#1. Simple Quiz Game 🎮
#Create a multiple-choice quiz with questions about Python, movies, or any fun topic! Display scores at the end and allow the user to play again. 🏆

def multiple_choice_quiz():
    # Function that states the questions, its choices, and answers
    questions = [
        {
            "Question": "What is the capital city of Kenya?",
            "Options": ["A. Kigali", "B. Nairobi", "C. Kisumu", "D. Kampala"],
            "Answer": "B"
        },
        {
            "Question": "When did Kenya gain independence?",
            "Options": ["A. 1964", "B. 1963", "C. 2000", "D. 1961"],
            "Answer": "B"
        },
        {
            "Question": "Who's the 5th president of Kenya?",
            "Options": ["A. William Ruto", "B. Mwai Kibaki", "C. Kithure Kindiki", "D. Uhuru Kenyatta"],
            "Answer": "A"
        },
    ]

    score = 0  # Initialize the score
    print("Welcome to the Quiz!!\n")

    # Loop through each question
    for i, q in enumerate(questions, start=1):
        print(f"Question {i}: {q['Question']}")
        for option in q["Options"]:
            print(option)
        user_name = input("Your answer (A/B/C/D): ").strip().upper()

        # Check the answer
        if user_name == q["Answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong answer! The correct answer was {q['Answer']}.\n")

    # Display the final score
    print(f"Quiz Complete! Your final score is {score}/{len(questions)}.")

# Run the quiz
multiple_choice_quiz()

