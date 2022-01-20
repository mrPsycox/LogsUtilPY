from cli import last_lines, first_lines, timestamps, ipv4, ipv6, highlight_text,check_primary_args,check_secondary_args,primary_args_handler,secondary_args_handler,arguments_handler, is_argument_set
import unittest
from colorama import Fore,Style

class first_lines_testclass(unittest.TestCase):
    def test_firstlines(self):

        text = ["primalinea 192.169.2.34 23:42:58\n","secondalinea 23:42:58 1.1.1.1 2607:f0d0:1002:0051:0000:0000:0000:0004\n","terzalinea2:22:44"]
        
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

        text = "primalinea 192.169.2.34 23:42:58\nsecondalinea\n3 00:14:23\nfourth line"

        with self.assertRaises(Exception) as context:
            timestamps([])        
        self.assertTrue('text must be a string' in str(context.exception))

        with self.assertRaises(Exception) as context2:
            timestamps(1)        
        self.assertTrue('text must be a string' in str(context2.exception))

        self.assertEqual(timestamps(text),"primalinea 192.169.2.34 23:42:58\n3 00:14:23")

        self.assertEqual(timestamps("primalineaa 192.169.2.3423:42:58\nsecondalinea\n300:14:23\nfourth line"),"primalineaa 192.169.2.3423:42:58\n300:14:23")

        self.assertEqual(timestamps("primalineaa192.169.2.3423;42:58\nsecondalinea\n300:14;23\nfourth line"),"")

        self.assertEqual(timestamps(""),"")

        self.assertEqual(timestamps("hi\nthere\nwow\n"), "")

class ipv4_testclass(unittest.TestCase):
    def test_ipv4(self):

        text = "primalinea 192.169.2.34 23:42:58\nsecondalinea\n3 00:14:23\nfourth line"

        with self.assertRaises(Exception) as context:
            ipv4([])        
        self.assertTrue('text must be a string' in str(context.exception))

        with self.assertRaises(Exception) as context2:
            ipv4(1)        
        self.assertTrue('text must be a string' in str(context2.exception))

        self.assertEqual(ipv4(text),"primalinea 192.169.2.34 23:42:58")

        self.assertEqual(ipv4("primalineaa 192.169.2.3423:42:58\nsecondalinea\n300:14:23\nfourth line"),"")

        self.assertEqual(ipv4("primalineaa192.169.2.3423;42:58\nsecondalinea\n300:14;23\nfourth line"),"")

        self.assertEqual(ipv4(""),"")

        self.assertEqual(ipv4("hi\nthere\nwow\n"), "")

class ipv6_testclass(unittest.TestCase):
    def test_ipv6(self):

        text = "primalinea 192.169.2.34 23:42:58\nsecondalinea\n3 00:14:23\nfourth line"
        text_withipv6 = "secondalinea 23:42:58 1.1.1.1 2607:f0d0:1002:0051:0000:0000:0000:0004\nquarta 00:00:00 2607:f0d0:1002:0051:0000:0000:0000:0004" 

        with self.assertRaises(Exception) as context:
            ipv6([])        
        self.assertTrue('text must be a string' in str(context.exception))

        with self.assertRaises(Exception) as context2:
            ipv6(1)        
        self.assertTrue('text must be a string' in str(context2.exception))

        self.assertEqual(ipv6(text),"")

        self.assertEqual(ipv6("primalineaa 192.169.2.3423:42:58\nsecondalinea\n300:14:23\nfourth line"),"")

        self.assertEqual(ipv6("primalineaa192.169.2.3423;42:58\nsecondalinea\n300:14;23\nfourth line"),"")

        self.assertEqual(ipv6(""),"")

        self.assertEqual(ipv6(text_withipv6),"secondalinea 23:42:58 1.1.1.1 2607:f0d0:1002:0051:0000:0000:0000:0004\nquarta 00:00:00 2607:f0d0:1002:0051:0000:0000:0000:0004")

        self.assertEqual(ipv6("hi\nthere\nwow\n"), "")

class highlighttext_testclass(unittest.TestCase):
    def test_highlighttext(self):

        with self.assertRaises(Exception) as context:
            highlight_text(12,[])        
        self.assertTrue('text must be a string' in str(context.exception))

        with self.assertRaises(Exception) as context1:
            highlight_text(["firststring","secondstring"],[])        
        self.assertTrue('text must be a string' in str(context1.exception))

        with self.assertRaises(Exception) as context2:
            highlight_text("cena",12)        
        self.assertTrue('secondary_args must be a list' in str(context2.exception))

        with self.assertRaises(Exception) as context3:
            highlight_text("cena","list")        
        self.assertTrue('secondary_args must be a list' in str(context3.exception))

        self.assertEqual(highlight_text(text="",secondary_args=[]),"")

        self.assertEqual(highlight_text("This line need to be colored: 127.0.0.1",["--ipv4"]),f'This line need to be colored: {Fore.RED}127.0.0.1 {Fore.RESET}')

        self.assertEqual(highlight_text("This line need to be colored: 127.0.0.n0\n2607:f0d0:1002:0051:0000:0000:0000:0004\n",["--ipv6"]),f'This line need to be colored: 127.0.0.n0\n{Fore.RED}2607:f0d0:1002:0051:0000:0000:0000:0004{Fore.RESET}\n')

class check_primary_args_testclass(unittest.TestCase):
    def test_check_primary_args(self):

        with self.assertRaises(Exception) as context:
            check_primary_args(12)        
        self.assertTrue('primary_args must to be a list.' in str(context.exception))

        self.assertCountEqual(check_primary_args(["-f","-l"]),["--first","--last"])

        self.assertCountEqual(check_primary_args(["-h","-l"]),["--last"])

        self.assertEqual(check_primary_args(["-q","-s"]),[])

    
class check_secondary_args_testclass(unittest.TestCase):
    def test_check_secondary_args(self):

        with self.assertRaises(Exception) as context:
            check_secondary_args(12)        
        self.assertTrue('secondary_args must to be a list.' in str(context.exception))

        self.assertCountEqual(check_secondary_args(["-f","-i"]),["--ipv4"])

        self.assertCountEqual(check_secondary_args(["-h","-t"]),["--timestamps"])

        self.assertCountEqual(check_secondary_args(["-h","-I"]),["--ipv6"])

        self.assertEqual(check_secondary_args(["-q","-s"]),[])


class primary_args_handler_testclass(unittest.TestCase):
    def test_primary_args_handler(self):

        with self.assertRaises(Exception) as context: 
            primary_args_handler(1,[])
        self.assertTrue('text must be a list of strings' in str(context.exception))


class secondary_args_handler_testclass(unittest.TestCase):
    def test_secondary_args_handler(self):

        with self.assertRaises(Exception) as context: 
            secondary_args_handler(1,[])
        self.assertTrue('text must be a list of strings' in str(context.exception))



class arguments_handler_testclass(unittest.TestCase):
    def test_arguments_handler(self):

        with self.assertRaises(Exception) as context: 
            arguments_handler(1)
        self.assertTrue('used_args must be a list' in str(context.exception))

        

class argument_set_testclass(unittest.TestCase):
    def test_argument_set(self):

        with self.assertRaises(Exception) as context: 
            is_argument_set(1)
        self.assertTrue('arg_name must be a string' in str(context.exception))




if __name__ == '__main__':
    unittest.main()
