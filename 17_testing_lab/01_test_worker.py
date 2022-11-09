


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
from unittest import TestCase, main


class WorkerTests(TestCase):
    def test_worker_initialization(self):
        worker = Worker("Test", 10000, 50)
        self.assertEqual("Test", worker.name)
        self.assertEqual(10000, worker.salary)
        self.assertEqual(50, worker.energy)
        self.assertEqual(0, worker.money)

    def test_energy_increment_after_rest(self):
        worker = Worker("Test", 10000, 50)
        self.assertEqual(50, worker.energy)
        worker.rest()
        self.assertEqual(51, worker.energy)

    def test_worker_work_with_zero_energy_raises(self):
        worker = Worker("Test", 10000, 0)
        with self.assertRaises(Exception) as exception:
            worker.work()
        self.assertEqual('Not enough energy.', str(exception.exception))

    def test_worker_with_negative_energy(self):
        worker = Worker("Test", 10000, -1)
        with self.assertRaises(Exception) as exception:
            worker.work()
        self.assertEqual('Not enough energy.', str(exception.exception))

    def test_if_worker_is_paid_after_work(self):
        worker = Worker("Test", 10000, 50)
        self.assertEqual(0, worker.money)
        worker.work()
        self.assertEqual(10000, worker.money)
        worker.work()
        self.assertEqual(20000, worker.money)

    def test_energy_decrease_after_work(self):
        worker = Worker("Test", 10000, 50)
        self.assertEqual(50, worker.energy)
        worker.work()
        self.assertEqual(49, worker.energy)

    def test_get_info(self):
        worker = Worker("Test", 10000, 50)
        expected = 'Test has saved 0 money.'
        self.assertEqual(expected, worker.get_info())

        worker.work()
        expected = 'Test has saved 10000 money.'
        self.assertEqual(expected, worker.get_info())


if __name__ == "__main__":
    unittest.main()

