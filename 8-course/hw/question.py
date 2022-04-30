class Question:

    def __init__(self, question, r_answer, difficulty, is_asked=False, user_answer=None):
        self.question = question
        self.difficulty = difficulty
        self.r_answer = r_answer
        self.points = difficulty * 10
        self.is_asked = is_asked
        self.user_answer = user_answer

    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return self.points

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответом иначе False.
        """
        if self.user_answer == self.r_answer:
            return True
        else:
            return False

    def build_question(self):
        return f"Вопрос {self.question}\n" \
               f"Сложность {self.difficulty}/5"

    # def ask(self):
    #     """Метод для тестирования"""
    #
    #     user_answer = input(f'{self.question}: ')
    #     if user_answer == self.r_answer:
    #         print("Ответ верный")
    #         print(f'вы получили {self.points} баллов')
    #     else:
    #         print("Ответ неверный")
    #         print("Верный:", self.r_answer)

    def build_feedback(self):
        """Дает пользователю обратную связь на ответ"""
        if self.is_correct():
            print("Ответ верный")
            print(f'вы получили {self.points} баллов')
        else:
            print("Ответ неверный")
            print("Верный:", self.r_answer)





