class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.person = Worker("Luc", 1000, 100)

    # def test_correct_initialization(self):
    #     result = self.person.name, self.person.salary, self.person.energy, self.person.money
    #     expected_result = "Luc", 1000, 100, 0
    #     self.assertEqual(expected_result, result)

    def test_correct_initialization(self):
        self.assertEqual("Luc", self.person.name)
        self.assertEqual(1000, self.person.salary)
        self.assertEqual(100, self.person.energy)
        self.assertEqual(0, self.person.money)

    def test_worker_energy_after_rest(self):
        self.person.rest()
        result = self.person.energy
        expected_result = 101
        self.assertEqual(expected_result, result)

    def test_worker_energy_with_negative_nrg(self):
        self.person.energy = 0
        with self.assertRaises(Exception) as ex:
            self.person.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_salary_after_work(self):
        self.person.work()
        result = self.person.money
        expected_result = 1000
        self.assertEqual(expected_result, result)

    def test_worker_energy_after_work(self):
        self.person.work()
        result = self.person.energy
        expected_result = 99
        self.assertEqual(expected_result, result)

    def test_worker_get_info(self):
        result = self.person.get_info()
        expected_result = f'Luc has saved 0 money.'
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()

