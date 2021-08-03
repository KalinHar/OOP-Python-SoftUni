from project.student import Student
from unittest import TestCase, main


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student('Viki', {"python": ["adv", 30], "Java": ["fnd", 20]})

    def test_non_courses_init(self):
        none_student = Student("Riki")
        self.assertEqual("Riki", none_student.family_name)
        self.assertEqual({}, none_student.courses)

    def test_with_courses_init(self):
        self.assertEqual("Viki", self.student.family_name)
        self.assertEqual({"python": ["adv", 30], "Java": ["fnd", 20]}, self.student.courses)

    def test_correct_leave_course(self):
        self.assertEqual("Course has been removed", self.student.leave_course("Java"))
        self.assertEqual({"python": ["adv", 30]}, self.student.courses)

    def test_incorrect_leave_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Go")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))
        self.assertEqual({"python": ["adv", 30], "Java": ["fnd", 20]}, self.student.courses)

    def test_correct_add_notes(self):
        self.assertEqual("Notes have been updated", self.student.add_notes("Java", "note"))
        self.assertEqual({"python": ["adv", 30], "Java": ["fnd", 20, "note"]}, self.student.courses)

    def test_incorrect_add_notes(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Go", ["note"])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))
        self.assertEqual({"python": ["adv", 30], "Java": ["fnd", 20]}, self.student.courses)

    def test_enroll_if_name_in_courses(self):
        self.assertEqual("Course already added. Notes have been updated.",
                         self.student.enroll("Java", ["adv", 30], "No"))
        self.assertEqual({"python": ["adv", 30], "Java": ["fnd", 20, "adv", 30]},
                         self.student.courses)

    def test_enroll_if_name_not_in_courses_but_yes(self):
        self.assertEqual("Course and course notes have been added.",
                         self.student.enroll("Go", ["adv", 30], "Y"))
        self.assertEqual({"python": ["adv", 30], "Java": ["fnd", 20], "Go": ["adv", 30]},
                         self.student.courses)
        new_student = Student('name', {'a': [1]})
        new_student.enroll('b', [1, 2])
        self.assertEqual({'a': [1], 'b': [1, 2]}, new_student.courses)

    def test_enroll_if_name_not_in_courses_and_not_add_notes(self):
        self.assertEqual("Course has been added.",
                         self.student.enroll("Go", ["adv", 30], "No"))
        self.assertEqual({"python": ["adv", 30], "Java": ["fnd", 20], "Go": []},
                         self.student.courses)


if __name__ == "__main__":
    main()
