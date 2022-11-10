import unittest
from project.student import Student


class StudentTests(unittest.TestCase):
    def setUp(self) -> None:
        self.student = Student("Name")

    def test_initialisation_without_courses(self):
        self.assertEqual("Name", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_initialisation_with_courses(self):
        test_student = Student("Name2", {"math": ["notes"]})
        self.assertEqual("Name2", test_student.name)
        self.assertEqual({"math": ["notes"]}, test_student.courses)

    def test_enroll_with_existing_course_add_notes(self):
        self.student.enroll("math", ["notes"])
        expected = "Course already added. Notes have been updated."
        actual = self.student.enroll("math", ["new_notes"])
        self.assertEqual(expected, actual)
        self.assertEqual({'math': ['notes', 'new_notes']}, self.student.courses)

    def test_enroll_with_existing_course_and_y(self):
        expected = "Course has been added."
        actual = self.student.enroll("math", ["new_notes"], "N")
        self.assertEqual(expected, actual)
        self.assertEqual({'math': []}, self.student.courses)

    def test_enroll_with_new_course_with_notes_y(self):
        expected = 'Course and course notes have been added.'
        actual = self.student.enroll("math", ["notes"], "Y")
        self.assertEqual(expected, actual)
        self.assertEqual({'math': ['notes']}, self.student.courses)

    def test_enroll_with_new_course(self):
        expected = 'Course and course notes have been added.'
        actual = self.student.enroll("math", ["notes"])
        self.assertEqual(expected, actual)
        self.assertEqual({'math': ['notes']}, self.student.courses)

    def test_enroll_with_new_course_and_no_notes(self):
        expected = 'Course has been added.'
        actual = self.student.enroll("math", ["notes"], "N")
        self.assertEqual(expected, actual)
        self.assertEqual({'math': []}, self.student.courses)

    def test_add_notes_existing_course(self):
        self.student.enroll("math", ["notes"])
        expected = 'Notes have been updated'
        actual = self.student.add_notes("math", "new notes")
        self.assertEqual(expected, actual)
        self.assertEqual({'math': ['notes', 'new notes']}, self.student.courses)

    def test_add_notes_no_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("math", "new notes")
        self.assertEqual('Cannot add notes. Course not found.', str(ex.exception))

    def test_leave_existing_course(self):
        self.student.enroll("math", ["notes"])
        expected = 'Course has been removed'
        actual = self.student.leave_course("math")
        self.assertEqual(expected, actual)
        self.assertEqual({}, self.student.courses)

    def test_leave_no_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("math")
        expected = 'Cannot remove course. Course not found.'
        self.assertEqual(expected, str(ex.exception))


if __name__ == "__main__":
    unittest.main()