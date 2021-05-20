from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for questions in question_data:
    text = questions["question"]
    answer = questions["correct_answer"]
    ques = Question(text, answer)
    question_bank.append(ques)


quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You have completed your quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
