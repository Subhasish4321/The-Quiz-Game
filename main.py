from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]

for questions in question_data:
    question_text=questions["question"]
    question_ans=questions["correct_answer"]
    new_question=Question(question_text,question_ans)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)
while quiz.still_have_questions():
    quiz.next_question()



