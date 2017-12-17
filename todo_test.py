import unittest
from usage_information import Usage
# import main_modul
import sys

my_object = Usage()

class TestUsage(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_print_usage(self):
        self.assertEqual(my_object.print_usage_information(),
            '\n'
            'Command Line Todo application\n'
            '=============================\n'
            '\n'        
            'Command Line arguments\n'
            '-l   Lists all the tasks\n'
            '-a   Adds a new task\n'
            '-r   Removes a task\n'
            '-c   Completes a task')

class MainModulTest(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
