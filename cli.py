#!/usr/bin/env python

#%%
import argparse
from argparse import RawTextHelpFormatter
import select
import sys


class ArgumentParserError(Exception): pass

class ThrowingArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise ArgumentParserError(message)

def first_lines():
    print("first function of PYTHONCLI app")

def last_lines():
    print("last function of PYTHONCLI app")

#HELPER FUNCTIONS --

#stdinput_check: check if stdin is empty or not. Return 1 if stdin is empty, 0 if not.
def stdinput_check():
    stdinput_flag = 0
    if select.select([sys.stdin,],[],[],0.0)[0]:
        stdinput_flag = 1
    return stdinput_flag

#is_argument_set: check if specific argument is specified or not. Return True if argument is specified, False if not.
def is_argument_set(arg_name):
    if arg_name in sys.argv:
        return True 
    return False

#check_parser_arguments: check if arguments are specified or not. Return the list of specified arguments, empty list if not.
def check_parser_arguments(args):
    target_args = ["--first","--last","--timestamps","--ipv4","--ipv6"]
    intersected_args = []
    for arg in target_args:
        if(is_argument_set(arg) == True):
            intersected_args.append(arg)
    return intersected_args


if __name__ == "__main__":
    parser = ThrowingArgumentParser()
    parser = argparse.ArgumentParser(description='Welcome to log parsing utility v1.02, a Python CLI application that will help you parse logs of various kinds.\n\n\nIf FILE is omitted, standard input is used instead.\nIf multiple options are used at once, the result is the intersection of their results.\nExample supported usage:\n------------------------\n./util.py -h\n<prints help>\n\ncat test_0.log | ./util.py --first 10\n<prints the first 10 lines of test_0.log>\n\n./utils.py --timestamps test_2.log\n<prints any lines from test_2.log that contain a timestamp>\n\n',formatter_class=RawTextHelpFormatter)
    parser.add_argument("--first",action='store',required=False,default=None, help="Print first NUM lines\n")
    parser.add_argument("--last",action='store',required=False,default=None, help="Print last NUM lines\n")
    parser.add_argument("--timestamps",action='store_true',required=False,default=None, help="Print lines that contain a timestamp in HH:MM:SS format\n")
    parser.add_argument("--ipv4",action='store_true',required=False,default=None, help="Print lines that contain an IPv4 address, matching IPs are highlighted\n")
    parser.add_argument("--ipv6",action='store_true',required=False,default=None, help="Print lines that contain an IPv6 address, matching IPs are highlighted\n")
    parser.add_argument("file",action='store',nargs='?',default=1, type=argparse.FileType('r'), help="Specify a file <filename>.log")

    args, unknown = parser.parse_known_args()
    

    stdin_flag = stdinput_check()

    used_args = check_parser_arguments(args)

    
    if(stdin_flag == 1 and args.file == 1):
        input_text = sys.stdin.readlines()
        print(input_text)
        #Here we work with the stdin text
    elif(stdin_flag == 0 and args.file != 1):
        print("aofra")
        #Here we work with the file specified as positional argument 
    elif(stdin_flag == 0 and args.file == 1):
        print("Bad usage: is possible to use STDIN or file, not both.\n")
        parser.print_help()
        exit(1)
    else:
        print("Bad usage: please specify <filename.log> or use STDIN to cli.py\n")
        parser.print_help()
        exit(1)

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