from project.factory.factory import Factory
from project.factory.paint_factory import PaintFactory
from unittest import TestCase, main


class TestPaintFactory(TestCase):
    def setUp(self):
        self.p_factory = PaintFactory("Color", 100)

    def test_init(self):
        self.assertEqual("Color", self.p_factory.name)
        self.assertEqual(100, self.p_factory.capacity)
        self.assertDictEqual({}, self.p_factory.ingredients)
        self.assertListEqual(["white", "yellow", "blue", "green", "red"],
                             self.p_factory.valid_ingredients)

    def test_property_products(self):
        self.assertEqual({}, self.p_factory.products)

    def test_can_add_value(self):
        self.p_factory.ingredients = {"white": 50, "yellow": 30}
        self.assertTrue(self.p_factory.can_add(20))
        self.assertFalse(self.p_factory.can_add(21))

    def test_repr_metod(self):
        self.p_factory.ingredients = {"white": 50, "yellow": 30}
        self.assertEqual("Factory name: Color with capacity 100.\n"
                         "white: 50\n"
                         "yellow: 30\n", repr(self.p_factory))

    def test_add_ingr_if_not_in_valid_ingr(self):
        with self.assertRaises(TypeError) as ex:
            self.p_factory.add_ingredient("black", 50)
        self.assertEqual("Ingredient of type black not allowed in PaintFactory",
                         str(ex.exception))

    def test_add_ingr_if_not_capacity(self):
        self.p_factory.ingredients = {"white": 50, "yellow": 30}
        with self.assertRaises(ValueError) as ex:
            self.p_factory.add_ingredient("red", 50)
        self.assertEqual("Not enough space in factory",
                         str(ex.exception))

    def test_add_ingr_correct(self):
        self.p_factory.add_ingredient("red", 50)
        self.assertDictEqual({"red": 50}, self.p_factory.ingredients)
        self.p_factory.add_ingredient("red", 20)
        self.assertDictEqual({"red": 70}, self.p_factory.ingredients)
        self.p_factory.add_ingredient("yellow", 30)
        self.assertDictEqual({"red": 70, "yellow": 30}, self.p_factory.ingredients)

    def test_remove_ingr_if_not_in_self_ingr(self):
        self.p_factory.ingredients = {"white": 50, "yellow": 30}
        with self.assertRaises(KeyError) as ex:
            self.p_factory.remove_ingredient("black", 50)
        self.assertEqual("'No such ingredient in the factory'",
                         str(ex.exception))

    def test_remove_ingr_if_not_quantity(self):
        self.p_factory.ingredients = {"white": 50, "yellow": 30}
        with self.assertRaises(ValueError) as ex:
            self.p_factory.remove_ingredient("white", 60)
        self.assertEqual("Ingredients quantity cannot be less than zero",
                         str(ex.exception))

    def test_remove_ingr_correct(self):
        self.p_factory.ingredients = {"white": 50, "yellow": 30}
        self.p_factory.remove_ingredient("white", 50)
        self.assertDictEqual({"white": 0, "yellow": 30}, self.p_factory.ingredients)


if __name__ == "__main__":
    main()
