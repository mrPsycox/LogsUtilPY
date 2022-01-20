# LogsUtilPY

# usage: cli.py [-h] [-f FIRST] [-l LAST] [-t] [-i] [-I] [file]

Welcome to log parsing utility v1.02, a Python CLI application that will help you parse logs of various kinds.

If FILE is omitted, standard input is used instead.
If multiple options are used at once, the result is the intersection of their results.
Example supported usage:
------------------------
./util.py -h
<prints help>

cat test_0.log | ./util.py --first 10
<prints the first 10 lines of test_0.log>

./utils.py --timestamps test_2.log
<prints any lines from test_2.log that contain a timestamp>

./util.py --ipv4 test_3.log
<prints any lines from test_3.log that contain an IPv4 address>

./util.py --ipv6 test_4.log
<prints any lines from test_4.log that contain an IPv6 address>

./util.py --ipv4 --last 50 test_5.log
<prints any of the last 50 lines from test_5.log that contain an IPv4 address>
==============================================================================

positional arguments:
  file                  Specify a file <filename>.log

optional arguments:
  -h, --help            show this help message and exit
  -f FIRST, --first FIRST
                        Print first NUM lines
  -l LAST, --last LAST  Print last NUM lines
  -t, --timestamps      Print lines that contain a timestamp in HH:MM:SS format
  -i, --ipv4            Print lines that contain an IPv4 address, matching IPs are highlighted
  -I, --ipv6            Print lines that contain an IPv6 address, matching IPs are highlighted
