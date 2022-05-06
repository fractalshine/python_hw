class BasicWord:

    def __init__(self, initial_word, subwords):
        self.initial_word = initial_word
        self.subwords = subwords

    def is_correct(self, user_input):
        if user_input in self.subwords:
            return True
        else:
            return False

    def get_len(self):
        return len(self.subwords)
