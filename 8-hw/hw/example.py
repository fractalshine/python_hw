class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check(self, user_answer):
        if user_answer == self.answer:
            return True
        else:
            return False

    def ask(self):
        user_answer = input(f'{self.question}: ')
        if user_answer == self.answer:
            print("Ответ верный")
        else:
            print("Ответ неверный")
            print("Верный:", self.answer)


questions = [
    Question("My name ___ Vova", "is"),
    Question("Who you ___?", "are"),
]
for q in questions:
    q.ask()
