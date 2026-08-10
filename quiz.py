import time

questions = [
    "what is the capital of India?",
    "Which planet is known as the Red Planet?",
    "How many days are there in a leap year?",
    "How many continents are there  on Earth?",
    "What is the smallest prime number?",
    "Which is the largest mammal in the world?",
    "How many colors are there in a rainbow?",
    "Which is the national bird of India?",
    "How many months are there in a year?",
    "Which festival is know as the Festival of Lights?"
]
options = [
    "A) Mumbai  B) Chennai  C) New Delhi  D) Kolkata",
    "A) Venus  B) Mars  C) Jupiter  D) Saturn",
    "A) 365  B) 366  C) 364  D) 360",
    "A) 5  B) 6  C) 7  D) 8",
    "A) 1  B) 2  C) 3  D) 5",
    "A) Elephant  B) Giraffe  C) Blue Whale  D) Hippopotamus",
    "A) 5  B) 6  C) 7  D) 8",
    "A) Parrot  B) Peacock  C) Sparrow  D) Eagle",
    "A) 10  B) 11  C) 12  D) 13",
    "A) Holi  B) Diwali  C) Eid  D) Christmas"
]
correct_answers = ["C", "B","B","C","B","C","C","B","C","B"]

time_limit = 5
score = 0
user_answers = []

print("--- Start Quiz ---")

for i in range(len(questions)):
    print(f"\nQuestion {i+1}: {questions[i]}")
    print(options[i])
    
    start = time.time()
    ans = input("Your answer (A, B, C, or D): ").strip().upper()
    end = time.time()
    
    if (end - start) > time_limit:
        user_answers.append("Time Out")
    else:
        user_answers.append(ans)
        if ans == correct_answers[i]:
            score += 1

print(f"\nFinal Score: {score}/{len(questions)}")
print("\n=== WRONG ANSWERS REVIEW ===")

has_wrong = False
for i in range(len(questions)):
    if user_answers[i] != correct_answers[i]:
        has_wrong = True
        print(f"\nQuestion {i+1}: {questions[i]}")
        print(f"Your Answer: {user_answers[i]}")
        print(f"Correct Answer: {correct_answers[i]}")

if not has_wrong:
    print("Perfect game! You didn't get any answers wrong.")
print("============================")