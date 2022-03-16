import unittest
from student import Student
from datetime import date, timedelta
from unittest.mock import patch
# to mock the API request


class TestStudent(unittest.TestCase):

    # method for the whole class, not only an instance
    # runs at the beginning 
    @classmethod
    def setUpClass(cls):
        print("set up class")

    # setup before each test
    def setUp(self):
        print("setup")
        self.student = Student("John", "Doe")

    # method for the whole class, not only an instance
    # runs at the end
    @classmethod
    def tearDownClass(cls):
        print("tear down Class")

    # tear down after each test
    def tearDown(self):
        print("tear down")

    def test_full_name(self):
        
        self.assertEqual(self.student.full_name, "John Doe")

    def test_alert_santa(self):
        
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)
    
    def test_email(self):
        
        self.assertEqual(self.student.email, "john.doe@email.com")
    
    def test_apply_extension(self):
        old_end_date = self.student.end_date
        self.student.apply_extension(14)
        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=14))
    
    # with the following two methods you mock an API call and test for both
    # a successful and unsuccessful call
    def test_course_schedule_success(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")
            
    def test_course_schedule_failed(self):
        """
        In the path "student" comes from the name of the file student.py
        If you have named the file something else - it will need to match
        eg, students.py would need "students.requests.get"
        """
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong")

if __name__ == "__main__":
    unittest.main()