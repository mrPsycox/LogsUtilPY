#!/usr/bin/env python

#%%
import argparse
from argparse import RawTextHelpFormatter
# import select
import sys


class ArgumentParserError(Exception): pass

class ThrowingArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise ArgumentParserError(message)

def first_lines():
    print("first function of PYTHONCLI app")

def last_lines():
    print("last function of PYTHONCLI app")


if __name__ == "__main__":
    parser = ThrowingArgumentParser()
    parser = argparse.ArgumentParser(description='Welcome to log parsing utility v1.02, a Python CLI application that will help you parse logs of various kinds.\n\n\nIf FILE is omitted, standard input is used instead.\nIf multiple options are used at once, the result is the intersection of their results.\nExample supported usage:\n------------------------\n./util.py -h\n<prints help>\n\ncat test_0.log | ./util.py --first 10\n<prints the first 10 lines of test_0.log>\n\n./utils.py --timestamps test_2.log\n<prints any lines from test_2.log that contain a timestamp>\n\n',formatter_class=RawTextHelpFormatter)
    parser.add_argument("--first",action='store',required=False,default=None, help="Print first NUM lines\n")
    parser.add_argument("--last",action='store',required=False,default=None, help="Print last NUM lines\n")
    parser.add_argument("--timestamps",action='store_true',required=False,default=None, help="Print lines that contain a timestamp in HH:MM:SS format\n")
    parser.add_argument("--ipv4",action='store_true',required=False,default=None, help="Print lines that contain an IPv4 address, matching IPs are highlighted\n")
    parser.add_argument("--ipv6",action='store_true',required=False,default=None, help="Print lines that contain an IPv6 address, matching IPs are highlighted\n")
    parser.add_argument("file", nargs='?',default=1, type=argparse.FileType('r'), help="Specify a file <filename>.log")

    args, unknown = parser.parse_known_args()

    # logs_text = ""

    #need to develop logical way to switch between stdin and positional file
    # stdin_state = False
    # if (select.select([sys.stdin,],[],[],0.0)[0]):
    #     logs_text = sys.stdin
    # else:
    #     pass


    #TODO 
    #STARTING FROM STDIN, WE CAN DIVIDE THE ALGORITHM IN TWO MAIN ROOT


    if(sys.stdin != None):
        #ROOT A
        print("ziopera")
    else:
        #ROOT B
        if(args.file.name != 1):
        print("ziosalame")







    # for lines in sys.stdin.readlines():
    #     print(lines)

    
    # with open(args.file.name, 'r') as f:
    #     log_lines = [line.strip() for line in f]
    
    # if(args.file == 1):
    #     print()
    # elif(args.first != None):
    #     #need to print first num lines of test.log
    #     print("I've to print the fist num lines")
    # elif(args.timestamps == True):
    #     print("I've to print timestamps")






# %%