questions = {
    "What is the capital of France?": "Paris",
    "Which language is primarily used for Android development?": "Kotlin",
    "What does CPU stand for?": "Central Processing Unit",
    "Who developed the theory of relativity?": "Einstein"
}

score = 0

print("🎮 Welcome to the Quiz Game!")
print("Answer the following questions:\n")

for question, answer in questions.items():
    user_answer = input(question + " ")
    if user_answer.strip().lower() == answer.lower():
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is {answer}\n")

print(f"Your final score is {score}/{len(questions)}")
