from project.hardware.hardware import Hardware
from project.software.software import Software
from unittest import TestCase, main


class TestHardware(TestCase):
    def setUp(self):
        self.hard = Hardware("HDD", "Power", 400, 1000)
        self.soft1 = Software("Linux", "Heavy", 200, 200)
        self.soft2 = Software("Windows", "Heavy", 500, 200)
        self.soft3 = Software("Windows", "Heavy", 200, 1200)

    def test_init(self):
        self.assertEqual("HDD", self.hard.name)
        self.assertEqual("Power", self.hard.type)
        self.assertEqual(400, self.hard.capacity)
        self.assertEqual(1000, self.hard.memory)
        self.assertListEqual([], self.hard.software_components)

    def test_correct_install(self):
        self.hard.install(self.soft1)
        self.assertEqual(400, self.hard.capacity)
        self.assertEqual(1000, self.hard.memory)
        self.assertListEqual([self.soft1], self.hard.software_components)

    def test_incorrect_install_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.hard.install(self.soft2)
        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_incorrect_install_memory(self):
        with self.assertRaises(Exception) as ex:
            self.hard.install(self.soft3)
        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_uninstall(self):
        self.hard.install(self.soft1)
        self.assertListEqual([self.soft1], self.hard.software_components)
        self.hard.uninstall(self.soft1)
        self.assertListEqual([], self.hard.software_components)
        self.assertEqual(400, self.hard.capacity)
        self.assertEqual(1000, self.hard.memory)


if __name__ == "__main__":
    main()
