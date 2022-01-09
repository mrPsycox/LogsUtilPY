from cli import last_lines, first_lines, timestamps, ipv4, ipv6
import unittest
import logging

class first_lines_testclass(unittest.TestCase):
    def test_firstlines(self):

#        
# class SomeTest( unittest.TestCase ):
#     def testSomething( self ):
#         log= logging.getLogger( "SomeTest.testSomething" )
#         log.debug( "this= %r", self.this )
#         log.debug( "that= %r", self.that )
#         # etc.
#         self.assertEquals( 3.14, pi )

# if __name__ == "__main__":
#     logging.basicConfig( stream=sys.stderr )
#     logging.getLogger( "SomeTest.testSomething" ).setLevel( logging.DEBUG )
#     unittest.main()

        with self.assertRaises(SystemExit) as code:
            first_lines([],numlines=1)
        self.assertEqual(code.exception.code, 1)

        with self.assertRaises(Exception) as context:
            first_lines([1,2,3,4,5],numlines=1)        
        self.assertTrue('text must be a list of string' in str(context.exception))

        with self.assertRaises(Exception) as context2:
            first_lines("ciaone\n",numlines=1)        
        self.assertTrue('text must be a list' in str(context.exception))


class last_lines_testclass(unittest.TestCase):
    def test_lastlines(self):
        with self.assertRaises(SystemExit) as code:
            last_lines([],numlines=1)
        self.assertEqual(code.exception.code, 1)

class timestamps_testclass(unittest.TestCase):
    def test_timestamps_emptytext(self):
        self.assertEqual(timestamps("hi\nthere\nwow\n"), "")

class ipv4_testclass(unittest.TestCase):
    def test_timestamps_emptytext(self):
        self.assertEqual(ipv4("hi\nthere\nwow\n"), "")

class ipv6_testclass(unittest.TestCase):
    def test_timestamps_emptytext(self):
        self.assertEqual(ipv6("hi\nthere\nwow\n"), "")

if __name__ == '__main__':
    unittest.main()
