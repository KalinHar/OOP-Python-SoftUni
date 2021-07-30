class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)
 
    def get_data(self):
        return self.__data
 
    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()
 
    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a
 
    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]
 
    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")
 
        self.get_data().insert(index, el)
 
    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]
 
    def get_index(self, el):
        return self.get_data().index(el)


import unittest


class IntegerListTests(unittest.TestCase):

    def setUp(self):
        self.nums = IntegerList(1, 2, "Tom", 3, [1, 2, 3], 10, 4)

    def test_nums_constructor(self):
        result = self.nums.get_data()
        exp_result = [1, 2, 3, 10, 4]
        self.assertEqual(result, exp_result)

    def test_add_int_element(self):
        result = self.nums.add(5)
        exp_result = [1, 2, 3, 10, 4, 5]
        self.assertEqual(result, exp_result)

    def test_add_non_int_element(self):
        with self.assertRaises(Exception):
            self.nums.add("element")

    def test_remove_correct_index(self):
        result = self.nums.remove_index(2)
        exp_result = 3
        self.assertEqual(result, exp_result)

    def test_remove_incorrect_index(self):
        with self.assertRaises(Exception):
            self.nums.remove_index(5)

    def test_get_correct_index(self):
        result = self.nums.get(1)
        exp_result = 2
        self.assertEqual(result, exp_result)

    def test_get_incorrect_index(self):
        with self.assertRaises(Exception):
            self.nums.get(5)

    def test_insert_correct_index_el(self):
        self.nums.insert(1, 100)
        result = self.nums.get_data()
        exp_result = [1, 100, 2, 3, 10, 4]
        self.assertEqual(result, exp_result)

    def test_insert_incorrect_index(self):
        with self.assertRaises(Exception):
            self.nums.insert(5, 100)

    def test_insert_incorrect_el(self):
        with self.assertRaises(Exception):
            self.nums.insert(1, "element")

    def test_get_biggest_el(self):
        result = self.nums.get_biggest()
        exp_result = 10
        self.assertEqual(result, exp_result)

    def test_get_index_of_el(self):
        result = self.nums.get_index(4)
        exp_result = 4
        self.assertEqual(result, exp_result)


if __name__ == "__main__":
    unittest.main()
