quiz = []

for i in range(1,6):
    quizzes = int(input(f"Enter Quiz {i} score: "))
    quiz.append(quizzes)

len_quiz = len(quiz)
sum_quiz = sum(quiz)
min_quiz = min(quiz)
max_quiz = max(quiz)
sort_quiz = sorted(quiz)
reverse_sort_quiz = sorted(quiz, reverse=True)

print("===== QUIZ SCORE REPORT =====")
print(f"Quiz Scores: {quiz}")
print("Number of Quizzes: 5")
print(f"Total Score: {sum_quiz}")
print(f"Average Score: {sum_quiz/len_quiz}")
print(f"Highest Score: {max_quiz}")
print(f"Lowest Score: {min_quiz}")
print(f"Ascending Score: {sort_quiz}")
print(f"Descending Score: {reverse_sort_quiz}")
print(f"Original Score: {quiz}")