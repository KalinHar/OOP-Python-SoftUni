# class dictionary_iter:
#     def __init__(self, dict_obj):
#         self.dict_obj = dict_obj
#         self.keys = list(dict_obj.keys())
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.keys:
#             result = self.keys[0], self.dict_obj[self.keys[0]]
#             self.keys.pop(0)
#             return result
#         raise StopIteration


class dictionary_iter:
    def __init__(self, dict_obj):
        self.dict_list = list(dict_obj.items())

    def __iter__(self):
        return self

    def __next__(self):
        while self.dict_list:
            return self.dict_list.pop(0)
        raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

