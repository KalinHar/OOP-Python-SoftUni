from project.vehicle import Vehicle
from unittest import TestCase, main


class TestVehicle(TestCase):
    def setUp(self):
        self.car = Vehicle(60, 100)

    def test_init(self):
        self.assertEqual(60, self.car.fuel)
        self.assertEqual(60, self.car.capacity)
        self.assertEqual(100, self.car.horse_power)
        self.assertEqual(1.25, self.car.fuel_consumption)

    def test_string_repr(self):
        self.assertEqual("The vehicle has 100 horse power with 60 fuel left and 1.25 fuel consumption",
                         self.car.__str__())

    def test_correct_drive(self):
        self.car.drive(4)
        self.assertEqual(55, self.car.fuel)

    def test_incorrect_drive(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(5000)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_correct_refuel(self):
        self.car.refuel(0)
        self.assertEqual(60, self.car.fuel)

    def test_incorrect_refuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(1)
        self.assertEqual("Too much fuel", str(ex.exception))


if __name__ == "__main__":
    main()
