class Player:

    def __init__(self, username):
        self.username = username
        self.used_words = []

    def count_used_words(self):
        return len(self.used_words)

    def add_used_word(self, user_input):
        self.used_words.append(user_input)
