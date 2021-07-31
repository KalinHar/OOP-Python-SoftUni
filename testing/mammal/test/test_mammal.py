from project.mammal import Mammal

from unittest import TestCase, main


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Tom", "cats", "meow")

    def test_initialization(self):
        self.assertEqual("Tom", self.mammal.name)
        self.assertEqual("cats", self.mammal.type)
        self.assertEqual("meow", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_make_sound(self):
        self.assertEqual("Tom makes meow", self.mammal.make_sound())

    def test_info(self):
        self.assertEqual("Tom is of type cats", self.mammal.info())


if __name__ == "__main__":
    main()