class QuizBrain:
    
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.number_of_questions = len(question_list)
        self.score = 0
    
    def still_has_question(self):
        return self.question_number < self.number_of_questions
    
    def next_question(self):
        
        current_question = self.question_list[self.question_number]
        self.question_number = self.question_number + 1
        user_ans = input(f"Q.{self.question_number} {current_question.text} (True/False) : ")
        correct_ans = current_question.answer
        
        self.check_answer(correct_ans=correct_ans, user_ans=user_ans)
    
    def check_answer (self, correct_ans, user_ans):
        
        if (correct_ans == user_ans):
            print("Answer was Correct")
            self.score = self.score + 1
        else:
            print("That was Wrong")
        
        print(f"Correct Answer is {correct_ans}")
        print(f"Score : {self.score}/{self.question_number}")
        print("\n")