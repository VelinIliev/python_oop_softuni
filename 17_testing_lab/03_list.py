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


from unittest import TestCase, main
import unittest


class IntegerListTests(TestCase):
    def test_add_with_correct_data(self):
        il = IntegerList(1, 2, 3)
        il.add(4)
        self.assertEqual([1, 2, 3, 4], il._IntegerList__data)

    def test_add_with_incorrect_data(self):
        il = IntegerList(1, 2, 3)
        with self.assertRaises(ValueError) as ve:
            il.add(3.2)
        self.assertEqual('Element is not Integer', str(ve.exception))

    def test_remove_index_correct(self):
        il = IntegerList(1, 2, 3)
        il.remove_index(2)
        self.assertEqual([1, 2], il._IntegerList__data)

    def test_remove_index_incorrect(self):
        il = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as ie:
            il.remove_index(3)
        self.assertEqual('Index is out of range', str(ie.exception))

    def test_init_with_correct_input(self):
        il = IntegerList(1, 2, 3)
        self.assertEqual([1, 2, 3], il._IntegerList__data)

    def test_init_with_incorrect_input(self):
        il = IntegerList(2.3, "A", False, None)
        self.assertEqual([], il._IntegerList__data)

    def test_get_with_correct(self):
        il = IntegerList(1, 2, 3)
        self.assertEqual(3, il.get(2))

    def test_get_with_incorrect_data(self):
        il = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as ie:
            il.get(3)
        self.assertEqual('Index is out of range', str(ie.exception))

    def test_insert_correct(self):
        il = IntegerList(1, 2, 3)
        il.insert(0, 0)
        self.assertEqual([0, 1, 2, 3], il._IntegerList__data)

    def test_insert_incorrect_index(self):
        il = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as ie:
            il.insert(3, 4)
        self.assertEqual('Index is out of range', str(ie.exception))

    def test_insert_incorrect_data(self):
        il = IntegerList(1, 2, 3)
        with self.assertRaises(ValueError) as ve:
            il.insert(0, 2.1)
        self.assertEqual('Element is not Integer', str(ve.exception))

    def test_get_biggest(self):
        il = IntegerList(1, 2, 3)
        self.assertEqual(3, il.get_biggest())

    def test_get_index(self):
        il = IntegerList(1, 2, 3)
        self.assertEqual(2, il.get_index(3))


if __name__ == "__main__":
    unittest.main()

