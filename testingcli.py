from cli import last_lines
import unittest

class first_lines_testclass(unittest.TestCase):
    def test_lastlines_emptytext(self):
        self.assertEqual(last_lines(["ciaone\n","pisellone\n","amostro\n"],1), "amostro")

if __name__ == '__main__':
    unittest.main()
    #print(last_lines(["ciaone\n","pisellone\n","amostro\n"],1))
