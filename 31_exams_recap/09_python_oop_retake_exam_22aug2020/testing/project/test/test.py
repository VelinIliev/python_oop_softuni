from unittest import TestCase, main

from project.student_report_card import StudentReportCard


class TestStudentReportCard(TestCase):
    def setUp(self) -> None:
        self.src = StudentReportCard("Ivan", 10)

    def test_initialization(self):
        self.assertEqual("Ivan", self.src.student_name)
        self.assertEqual(10, self.src.school_year)
        self.assertEqual({}, self.src.grades_by_subject)

    def test_test_initialization_with_empty_string_name_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.src.student_name = ""
        self.assertEqual("Student Name cannot be an empty string!", str(ve.exception))
        self.assertEqual("Ivan", self.src.student_name)

    def test_school_year_with_valid_year(self):
        self.src.school_year = 1
        self.assertEqual(1, self.src.school_year)
        self.src.school_year = 12
        self.assertEqual(12, self.src.school_year)

    def test_test_initialization_with_non_valid_school_year_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.src.school_year = 0
        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))
        self.assertEqual(10, self.src.school_year)
        with self.assertRaises(ValueError) as ve:
            self.src.school_year = 13
        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))
        self.assertEqual(10, self.src.school_year)

    def test_add_grade_with_non_existing_subject(self):
        self.src.add_grade("Math", 3.00)
        self.src.add_grade("History", 5.25)
        self.assertEqual({'Math': [3.0], "History": [5.25]}, self.src.grades_by_subject)

    def test_add_grade_with_existing_subject(self):
        self.src.add_grade("Math", 3.00)
        self.src.add_grade("Math", 5.00)
        self.assertEqual({'Math': [3.0, 5.0]}, self.src.grades_by_subject)

    def test_average_grade_by_subject(self):
        self.src.add_grade("Math", 3.00)
        self.src.add_grade("Math", 5.00)
        self.src.add_grade("History", 3.00)
        self.src.add_grade("History", 5.00)
        expected = f'Math: 4.00\nHistory: 4.00'
        actual = self.src.average_grade_by_subject()
        self.assertEqual(expected, actual)

    def test_average_grade_for_all_subject(self):
        self.src.add_grade("Math", 3.00)
        self.src.add_grade("Math", 5.00)
        self.src.add_grade("History", 3.00)
        self.src.add_grade("History", 5.00)
        expected = 'Average Grade: 4.00'
        actual = self.src.average_grade_for_all_subjects()
        self.assertEqual(expected, actual)

    def test_repr(self):
        self.src.add_grade("Math", 3.00)
        self.src.add_grade("Math", 5.00)
        self.src.add_grade("History", 3.00)
        self.src.add_grade("History", 5.00)
        expected = "Name: Ivan\n" \
                   "Year: 10\n" \
                   "----------\n" \
                   "Math: 4.00\n" \
                   "History: 4.00\n" \
                   "----------\n" \
                   "Average Grade: 4.00"
        actual = self.src.__repr__()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
