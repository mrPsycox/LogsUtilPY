from cli import last_lines
import unittest

class first_lines_testclass(unittest.TestCase):
    def test_lastlines_emptytext(self):
        self.assertEqual(last_lines(["hi\n","there\n","wow\n"],1), "wow")

if __name__ == '__main__':
    unittest.main()
