class CharCounter:
    def __init__(self, word):
        self.word = word

    def count_occurrences(self):
        char_count = {}
        for i in self.word:
            if i in char_count:
                char_count[i] += 1
            else:
                char_count[i] = 1
        return char_count

w = "apperance"
counter = CharCounter(w)
print(counter.count_occurrences())
