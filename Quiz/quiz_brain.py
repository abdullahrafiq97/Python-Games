class QuizBrain:
    def __init__(self, list):
        self.n = 0
        self.list = list
        self.score = 0

    def still_has_question(self):
        if self.n<len(self.list):
            return True
        else:
            return False

    def next_question(self):
        qstn = self.list[self.n]
        self.n+=1
        ans = input(f"Q.{self.n} {qstn.text} (True/False): ")
        self.check_answer(ans, qstn.answer)

    def check_answer(self, user_ans, corr_ans):
        if user_ans.lower() == corr_ans.lower():
            print("You are right!")
            self.score += 1
            print(f"Your current score is {self.score}/{self.n}")
        else:
            print("Sorry. That is incorrect!")
            print(f"Your current score is {self.score}/{self.n}")