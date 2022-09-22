from hashlib import new
from Day17.quiz_brain import quiz_brain
from question_model import question
from data import question_data
from quiz_brain import quiz_brain

question_bank = []

for temp in question_data:
    question_text = temp['text']
    question_answer = temp['answer']
    new_question = question(question_text, question_answer)
    question_bank.append(new_question)

QuizBrain = quiz_brain(question_bank)
while QuizBrain.still_has_questions():
    QuizBrain.next_question()

print("You've completed the quiz!")
print(f'Your final score was: {QuizBrain.score}/{QuizBrain.question_number}')