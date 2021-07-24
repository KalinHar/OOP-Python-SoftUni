from collections import deque


class vowels:
    def __init__(self, text):
        self.text_vowels = deque(char for char in text if char in "AaEeIiOoUuYy")

    def __iter__(self):
        return self

    def __next__(self):
        if self.text_vowels:
            return self.text_vowels.popleft()
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
