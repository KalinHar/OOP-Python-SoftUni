def reverse_text(text):
    text_as_list = list(text)
    while text_as_list:
        yield text_as_list.pop()


for char in reverse_text("step"):
    print(char, end='')
