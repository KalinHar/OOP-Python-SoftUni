from collections import deque

class vowels:
    vowels = "AaEeIiOoUuYy"

    def __init__(self, text):
        self.text = deque(text)

    def __iter__(self):
        return self

    def __next__(self):
        while self.text:
            char = self.text.popleft()
            if char in self.vowels:
                return char
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
