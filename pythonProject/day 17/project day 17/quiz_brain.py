class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.score = 0
        self.questionlist = question_list

    def still_has_question(self):
        return self.question_number < len(self.questionlist)

    def next_question(self):
        current_question = self.questionlist[self.question_number]
        self.question_number += 1
        a= input(f"Q.{self.question_number} : {current_question.text} (True/False): ")
        correct_answer = current_question.answer
        self.check_answer(a,correct_answer)

    def check_answer(self,u_answer,c_answer):
        if  c_answer.lower() == u_answer.lower() :
            print("You got it Right!")
            self.score += 1
        else:
            print("You got it wrong!")

        print(f"Correct answer was : {c_answer}")
        return print(f"{self.score}/{self.question_number}")


