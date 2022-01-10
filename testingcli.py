from typing import Text
from cli import last_lines, first_lines, timestamps, ipv4, ipv6
import unittest
import logging

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

class first_lines_testclass(unittest.TestCase):
    def test_firstlines(self):

        text = ["primalineaaaaaaaaaaaaaaaaaaaaaaaa 192.169.2.34 23:42:58\n","secondalinea 23:42:58 1.1.1.1 2607:f0d0:1002:0051:0000:0000:0000:0004\n","terzalinea2:22:44"]

        with self.assertRaises(SystemExit) as code:
            first_lines([],numlines=1)
        self.assertEqual(code.exception.code, 1)

        with self.assertRaises(Exception) as context:
            first_lines([1,2,3,4,5],numlines=1)        
        self.assertTrue('text must be a list of string' in str(context.exception))

        with self.assertRaises(Exception) as context2:
            first_lines("ciaone\n",numlines=1)        
        self.assertTrue('text must be a list' in str(context2.exception))

        with self.assertRaises(Exception) as context3:
            first_lines([1,2,3,4,"miao\n"],numlines=1)        
        self.assertTrue('text must be a list of string' in str(context3.exception))

        with self.assertRaises(Exception) as context3:
            first_lines(["ok\n",2,3,4,"miao\n"],numlines=2)        
        self.assertTrue('text must be a list of string' in str(context3.exception))

        self.assertEqual(first_lines(["ok\n",2,3,4,"miao\n"],numlines=1),"ok")

        with self.assertRaises(SystemExit) as code2:
            first_lines(["ok\n",2,3,4,"miao\n"],numlines=12)
        self.assertEqual(code2.exception.code, 1)

        self.assertEqual(first_lines(text,numlines=1),text[0].strip())


class last_lines_testclass(unittest.TestCase):
    def test_lastlines(self):

        text = ["primalineaaaaaaaaaaaaaaaaaaaaaaaa 192.169.2.34 23:42:58\n","secondalinea 23:42:58 1.1.1.1 2607:f0d0:1002:0051:0000:0000:0000:0004\n","terzalinea2:22:44\n"]

        with self.assertRaises(SystemExit) as code:
            last_lines([],numlines=1)
        self.assertEqual(code.exception.code, 1)

        with self.assertRaises(Exception) as context:
            last_lines([1,2,3,4,5],numlines=1)        
        self.assertTrue('text must be a list of string' in str(context.exception))

        with self.assertRaises(Exception) as context2:
            last_lines("ciaone\n",numlines=1)        
        self.assertTrue('text must be a list' in str(context2.exception))

        with self.assertRaises(Exception) as context3:
            last_lines([1,2,3,4,"miao\n"],numlines=2)        
        self.assertTrue('text must be a list of string' in str(context3.exception))

        self.assertEqual(last_lines([1,2,3,4,"miao\n"],numlines=1),"miao")

        with self.assertRaises(SystemExit) as code2:
            last_lines(["ok\n",2,3,4,"miao\n"],numlines=12)
        self.assertEqual(code2.exception.code, 1)

        self.assertEqual(last_lines(text,numlines=1),text[-1].strip())



class timestamps_testclass(unittest.TestCase):
    def test_timestamps(self):

        text = "primalineaaaaaaaaaaaaaaaaaaaaaaaa 192.169.2.34 23:42:58\nsecondalinea\n3 00:14:23\nfourth line"

        with self.assertRaises(Exception) as context:
            timestamps([])        
        self.assertTrue('text must be a string' in str(context.exception))

        with self.assertRaises(Exception) as context2:
            timestamps(1)        
        self.assertTrue('text must be a string' in str(context2.exception))

        self.assertEqual(timestamps(text),"primalineaaaaaaaaaaaaaaaaaaaaaaaa 192.169.2.34 23:42:58\n3 00:14:23")

        self.assertEqual(timestamps("primalineaaaaaaaaaaaaaaaaaaaaaaaa192.169.2.3423:42:58\nsecondalinea\n300:14:23\nfourth line"),"primalineaaaaaaaaaaaaaaaaaaaaaaaa192.169.2.3423:42:58\n300:14:23")

        self.assertEqual(timestamps("primalineaaaaaaaaaaaaaaaaaaaaaaaa192.169.2.3423;42:58\nsecondalinea\n300:14;23\nfourth line"),"")

        self.assertEqual(timestamps(""),"")


        self.assertEqual(timestamps("hi\nthere\nwow\n"), "")

class ipv4_testclass(unittest.TestCase):
    def test_ipv4(self):
        self.assertEqual(ipv4("hi\nthere\nwow\n"), "")

class ipv6_testclass(unittest.TestCase):
    def test_ipv6(self):
        self.assertEqual(ipv6("hi\nthere\nwow\n"), "")

if __name__ == '__main__':
    unittest.main()
