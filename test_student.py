import unittest
from student import student

class teststudent(unittest.TestCase):

    """def setUp(self):
        print("\nsetUp")
        std1 = student("divite", "vanitha", 21)
        std2 = student("allu", "dhana", 23)
    def tearDown(self):
        print('\ntearDown')"""

    def test_email(self):
        std1=student("divite","vanitha",21)
        std2=student("allu","dhana",23)
        self.assertEqual(std1.email,'divite.vanitha@gmail.com')
        self.assertEqual(std2.email,'allu.dhana@gmail.com')
        print("test_email")
    def test_fullname(self):
        std1 = student("divite", "vanitha", 21)
        std2 = student("allu", "dhana", 23)
        self.assertEqual(std1.fullname, 'divite vanitha')
        self.assertEqual(std2.fullname, 'allu dhana')
        print("test_fullname")
    def test_apply_bonus(self):
        std1=student("vanitha","divite",50)
        self.assertEqual(std1.marks,50)
        std1.apply_bonus()
        self.assertEqual(std1.marks,75)
        print("test_apply_bonus")
    def test_dummy(self):
        std1=student("vanitha","divite",75)
        self.assertEqual(std1.value,"")
        std1.dummy(10)
        self.assertEqual(std1.value,185,185)

if __name__ =="__main__":
    unittest.main()