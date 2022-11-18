from project.student_report_card import StudentReportCard

from typing import Dict, List
import unittest


class StudentReportCardTests(unittest.TestCase):
    def setUp(self) -> None:
        self.student_report = StudentReportCard("Ivan", 3)

    def test_initialisation(self):
        self.assertEqual("Ivan", self.student_report.student_name)
        self.assertEqual(3, self.student_report.school_year)
        self.assertEqual({}, self.student_report.grades_by_subject)

    def test_initialisation_with_wrong_name(self):
        with self.assertRaises(ValueError) as ve:
            self.student_report.student_name = ""
        expected = 'Student Name cannot be an empty string!'
        self.assertEqual(expected, str(ve.exception))

    def test_initialisation_wit_wrong_years(self):
        with self.assertRaises(ValueError) as ve:
            self.student_report.school_year = 0
        expected = "School Year must be between 1 and 12!"
        self.assertEqual(expected, str(ve.exception))
        with self.assertRaises(ValueError) as ve:
            self.student_report.school_year = 13
        self.assertEqual(expected, str(ve.exception))

    def test_add_grade(self):
        self.student_report.add_grade("Math", 5.0)
        self.student_report.add_grade("Math", 3.0)
        self.student_report.add_grade("Biology", 6.0)
        self.assertEqual({'Math': [5.0, 3.0], 'Biology': [6.0]}, self.student_report.grades_by_subject)

    def test_average_grade_by_subject(self):
        self.student_report.add_grade("Math", 5.0)
        self.student_report.add_grade("Math", 3.0)
        self.student_report.add_grade("Biology", 6.0)
        expected = 'Math: 4.00\nBiology: 6.00'
        actual = self.student_report.average_grade_by_subject()
        self.assertEqual(expected, actual)

    def test_average_for_all_subjects(self):
        self.student_report.add_grade("Math", 5.0)
        self.student_report.add_grade("Math", 3.0)
        self.student_report.add_grade("Biology", 6.0)
        expected = 'Average Grade: 4.67'
        actual = self.student_report.average_grade_for_all_subjects()
        self.assertEqual(expected, actual)

    def test__repr__(self):
        self.student_report.add_grade("Math", 5.0)
        self.student_report.add_grade("Math", 3.0)
        self.student_report.add_grade("Biology", 6.0)
        expected = "Name: Ivan\n" \
                   "Year: 3\n" \
                   "----------\n" \
                   "Math: 4.00\n" \
                   "Biology: 6.00\n" \
                   "----------\n" \
                   "Average Grade: 4.67"
        actual = self.student_report.__repr__()
        self.assertEqual(expected, actual)

#TODO: NOt ready