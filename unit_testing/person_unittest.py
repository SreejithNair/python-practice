import unittest
from person import Person

class PersonUnitTest(unittest.TestCase):
    """
    This test class will consider functions those start wih 'test' to run as test method
    All other functions will be considered as normal function.
    """
    def setUp(self): #setup object before running the test. Similar to test initializer 
        self.name='Sreejith'
        self.wrong_name='Bob'
    def test_exception(self):
        self.assertRaises(TypeError,Person)

    def otherfunction(self):
        print('some one called me')
    
    def test_name(self):
        ins = Person(self.name)
        name_returned = ins.get_name()
        self.assertEqual(self.name,name_returned)

    def test__wrong_name(self):
            ins = Person(self.name)
            name_returned = ins.get_name()
            self.assertNotEqual(self.wrong_name,name_returned)

if __name__ == "__main__":
    unittest.main()
