from ...project.train.train import Train
from unittest import TestCase, main


class TestTrain(TestCase):
    def setUp(self):
        self.tr = Train("exp", 100)

    def test_init(self):
        self.assertEqual("exp", self.tr.name)
        self.assertEqual(100, self.tr.capacity)
        self.assertEqual([], self.tr.passengers)
        self.assertEqual(0, Train.ZERO_CAPACITY)

    def test_add_correct(self):
        self.assertEqual("Added passenger Hoho", self.tr.add("Hoho"))
        self.assertEqual(["Hoho"], self.tr.passengers)

    def test_add_full_train(self):
        self.tr.capacity = 1
        self.tr.add("Hoho")
        with self.assertRaises(ValueError) as ex:
            self.tr.add("Hoho")
        self.assertEqual("Train is full", str(ex.exception))
        self.assertEqual(["Hoho"], self.tr.passengers)

    def test_add_same_passenge(self):
        self.tr.add("Hoho")
        with self.assertRaises(ValueError) as ex:
            self.tr.add("Hoho")
        self.assertEqual("Passenger Hoho Exists", str(ex.exception))
        self.assertEqual(["Hoho"], self.tr.passengers)

    def test_remove_correct(self):
        self.tr.add("Hoho")
        self.assertEqual("Removed Hoho",
                         self.tr.remove("Hoho"))
        self.assertEqual([], self.tr.passengers)

    def test_remove_if_not_passenger(self):
        self.tr.add("Hoho")
        with self.assertRaises(ValueError) as ex:
            self.tr.remove("Boho")
        self.assertEqual("Passenger Not Found", str(ex.exception))
        self.assertEqual(["Hoho"], self.tr.passengers)


if __name__ == '__main__':
    main()
