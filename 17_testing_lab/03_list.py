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
    def test_add_integer(self):
        il = IntegerList(1, 2, 3)
        with self.assertRaises(ValueError) as value_error:
            il.add(2.1)
        self.assertEqual('Element is not Integer', str(value_error.exception))

    def test_remove_index_out_of_range(self):
        il = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as index_error:
            il.remove_index(4)
        self.assertEqual('Index is out of range', str(index_error.exception))

    def test_init_taking_only_integers(self):
        il = IntegerList(1, 2.3, "A", False, None)
        self.assertEqual([1], il.get_data())

    def test_get_out_of_range(self):
        il = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as index_error:
            il.get(4)
        self.assertEqual('Index is out of range', str(index_error.exception))

    def test_insert_out_of_range(self):
        il = IntegerList(1, 2, 3)
        il.get_data()
        with self.assertRaises(IndexError) as index_error:
            il.insert(4, 2)
        self.assertEqual('Index is out of range', str(index_error.exception))

    def test_insert_element_not_integer(self):
        il = IntegerList(1, 2, 3)
        print(il.get_data())
        with self.assertRaises(ValueError) as value_error:
            il.insert(1, 2.1)
        self.assertEqual('Element is not Integer', str(value_error.exception))


if __name__ == "__main__":
    unittest.main()