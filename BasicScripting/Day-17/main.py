from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_list=question_bank)

while quiz_brain.still_has_question():
    quiz_brain.next_question()

print("you have Completed the Quiz")
print(f"The Finial Score was {quiz_brain.score}/{quiz_brain.number_of_questions}")