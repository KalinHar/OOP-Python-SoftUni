def vowel_filter(function):
    def wrapper():
        return [w for w in function() if w.lower() in "aeoui"]
    return wrapper


@vowel_filter
def get_letters():
    return ['a', 'b', 'c', 'd', 'e']


print(get_letters())
