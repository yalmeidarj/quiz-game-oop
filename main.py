from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from replit import clear

question_bank = []

for q in question_data:
    question_text = q["question"]
    question_answer = q["correct_answer"]
    new_question = Question(question_text, question_answer)
    new_list = (new_question.text, new_question.answer)
    question_bank.append(new_list)


quiz = QuizBrain(question_bank)
while len(question_bank) - 1 > quiz.question_number:
    quiz.next_question()
    clear()
else:
    quiz.next_question()
    clear()
    print(f"You've completed the quiz. Your final score is:{quiz.score}/{quiz.question_number}") 