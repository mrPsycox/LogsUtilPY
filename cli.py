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

def first_lines(text,numlines):
    print("first function of PYTHONCLI app\n")
    if(type(int(numlines)) is not int):
        print("--first option need a whole number to be executed! \n Please try again passing an int value\n")
        exit(1)
    
    ret = ""

    i = 0

    #TODO
    #create a loop that iterate text numlines times. Need to check it (check itertools library!)
    # while(i < type(int(numlines))):
    #     print(i)
    #     ret += text[i]
    #     i += 1

    return ret

def last_lines(text,numlines):
    print("last function of PYTHONCLI app")

def timestamps(text):
    print("timestamps function of PYTHONCLI app")


#HELPER FUNCTIONS --

#arguments_handler: from user_args, divide primary options to secondary options
def arguments_handler(used_args):
    target_args = ["--first","--last","--timestamps","--ipv4","--ipv6"]
    priority_args = []
    secondary_args = []
    for arg in target_args:
        if(arg in used_args and arg == "--first"):
            priority_args.append(arg)
        elif(arg in used_args and arg == "--last"):
            priority_args.append(arg)
        elif(arg in used_args and arg == "--timestamps"):
            secondary_args.append(arg)
        elif(arg in used_args and arg == "--ipv4"):
            secondary_args.append(arg)
        elif(arg in used_args and arg == "--ipv6"):
            secondary_args.append(arg)
        else:
            pass
    return priority_args,secondary_args

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

    #here we have the list with arguments used
    used_args = check_parser_arguments(args)

    if(stdin_flag == 1 and args.file == 1):
        #Here we work with the stdin text
        input_text = sys.stdin.readlines()
        args_check = arguments_handler(used_args)
        primary_args = args_check[0]
        secondary_args = args_check[1]
        
        if("--first" in primary_args and "--last" in primary_args):
            input_text_first = first_lines(input_text,args.first)
            print(input_text_first)


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


# %%