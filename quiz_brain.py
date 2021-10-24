class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        # q_list = len(question_bank)
        self.question_list = q_list

    def next_question(self):
        """Brings new question from data. stores user and correct answer."""
        current_number = self.question_number
        current_question = self.question_list[self.question_number][0]
        correct_answer = self.question_list[self.question_number][1]
        # current_score = self.score
        current_number += 1
        user_answer = input(f"Q.{current_number}:\n{current_question} Type --> True / False. Score: {self.score}/{self.question_number}").lower()
        self.question_number += 1
        self.check_answer(user_answer, correct_answer)

    def check_answer(self, user_answer, correct_answer):
        """Check answer and updates score."""
        self.user_answer = user_answer
        self.correct_answer = correct_answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right.")
        elif user_answer.lower() != correct_answer.lower():
            print("Wrong")
        print(f"The correct answer is: {correct_answer}")
        print(f"The current score is: {self.score}")
        print("\n")