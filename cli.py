#!/usr/bin/env python
#%%
import argparse
from argparse import RawTextHelpFormatter
import select
import sys
import re
from colorama import Fore

class ArgumentParserError(Exception): pass

class ThrowingArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise ArgumentParserError(message)

def first_lines(text,numlines):
    if(type(text) is not list):
        raise TypeError("text must be a list")
    if(type(int(numlines)) is not int):
        raise TypeError("numlines must be an int")
    n = int(numlines)
    if(n >= len(text)):
        print("Input text doesn't have %d lines. Please insert a valid value\n" % (n,))
        exit(1)
    tmp = str()
    i = 0
    for i in range(0,n):
        if(type(text[i]) is not str):
            raise TypeError("text must be a list of string")
        else:
            tmp += text[i]

    return tmp.strip()

#%%
def last_lines(text,numlines):
    if(type(text) is not list):
        raise TypeError("text must be a list")
    if(type(int(numlines)) is not int):
        raise TypeError("numlines must be an int")
    n = int(numlines)
    if(n > len(text)):
        print("Input text doesn't have %d lines. Please insert a valid value\n" % (n,))
        exit(1)
    ret = str()
    last_lines = text[-n:]
    for i in range(0,len(last_lines)):
        if(type(last_lines[i]) is not str):
             raise TypeError("text must be a list of string")
        else:
            ret += last_lines[i]

    return ret.strip()


#%%
def timestamps(text):
    if(type(text) is not str):
        raise TypeError("text must be a string")
    ret =""
    finds = re.findall("^.*(?:[01]\d|2[0123]):(?:[012345]\d):(?:[012345]\d).*",text,re.MULTILINE)
    if(len(finds) == 0):
        pass
    else:
        for line in finds:
            ret += (line + "\n")
    return ret.strip()

def ipv4(text):
    if(type(text) is not str):
        raise TypeError("text must be a string")
    ret = ""
    ipv4_regex = r'''.*(?:^|\b(?<!\.))(?:1?\d?\d|2[0-4]\d|25[0-5])(?:\.(?:1?\d?\d|2[0-4]\d|25[0-5])){3}(?=$|[^\w.]).*'''
    finds = re.findall(ipv4_regex,text,re.MULTILINE)
    if(len(finds) == 0):
        pass
    else:
        for line in finds:
            ret += (line + "\n")
    return ret

def ipv6(text):
    if(type(text) is not str):
        raise TypeError("text must be a string")
    ret = ""
    for line in text.split("\n"):
        if(re.match("^.*(?:^|(?<=\s))(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))(?=\s|$).*",line)):
            ret += (line + "\n")
        else:
            pass
    return ret

#HELPER FUNCTIONS --
def check_primary_args(primary_args):
    ret = []
    for i, word in enumerate(primary_args):
        if(word == "-f"):
            primary_args[i] = "--first"
        elif(word == "-l"):
            primary_args[i] = "--last"
        else:
            pass

    ret = list(set(primary_args))
    return ret


def check_secondary_args(secondary_args):
    ret = []
    for j, word in enumerate(secondary_args):
        if(word == "-t"):
            secondary_args[j] = "--timestamps"
        elif(word == "-i"):
            secondary_args[j] = "--ipv4"
        elif(word == "-I"):
            secondary_args[j] = "--ipv6"
        else:
            pass
    ret = list(set(secondary_args))
    return ret
    

def primary_args_handler(text,primary_args):
    final_text = ""
    if("--first" in primary_args and "--last" in primary_args):
        input_text_first = first_lines(text,args.first)
        final_text += input_text_first
        final_text += "\n"
        input_text_last = last_lines(text,args.last)
        final_text += input_text_last
    elif("--first" in primary_args and "--last" not in primary_args):
        input_text_first_tmp = first_lines(text,args.first)
        final_text += input_text_first_tmp
    elif("--first" not in primary_args and "--last" in primary_args):
        input_text_last_tmp = last_lines(text,args.last)
        final_text += input_text_last_tmp
    else:
        pass
    return final_text


def secondary_args_handler(text,secondary_args):
    final_text = ""
    if("--timestamps" in secondary_args and "--ipv4" not in secondary_args and "--ipv6" not in secondary_args):
        timestamps_ret = timestamps(text)
        final_text += timestamps_ret
    elif("--timestamps" not in secondary_args and "--ipv4" in secondary_args and "--ipv6" not in secondary_args):
        ipv4_ret = ipv4(text)
        final_text += ipv4_ret
    elif("--timestamps" not in secondary_args and "--ipv4" not in secondary_args and "--ipv6" in secondary_args):
        ipv6_ret = ipv6(text)
        final_text += ipv6_ret        
    elif("--timestamps" in secondary_args and "--ipv4" in secondary_args and "--ipv6" not in secondary_args):
        timestamps_ret_text = timestamps(text)
        ipv4_merged_text = ipv4(timestamps_ret_text)
        final_text += ipv4_merged_text
    elif("--timestamps" in secondary_args and "--ipv4" not in secondary_args and "--ipv6" in secondary_args):
        timestamps_ret_text = timestamps(text)
        ipv6_merged_text = ipv6(timestamps_ret_text)
        final_text += ipv6_merged_text
    elif("--timestamps" not in secondary_args and "--ipv4" in secondary_args and "--ipv6" in secondary_args):
        ipv4_merged_text = ipv4(text)
        ipv6_merged_text = ipv6(ipv4_merged_text)
        final_text += ipv6_merged_text      
    elif("--timestamps" in secondary_args and "--ipv4" in secondary_args and "--ipv6" in secondary_args):
        timestamps_ret = timestamps(text)
        ipv4_merged_text = ipv4(timestamps_ret)
        ipv6_merged_text = ipv6(ipv4_merged_text)
        final_text += ipv6_merged_text

    highlighted_final_text = highlight_text(final_text,secondary_args)
    
    return highlighted_final_text
    #return final_text

def highlight_text(text,secondary_args):
    ipv4_regex = re.compile(r'(?:^|\b(?<!\.))(?:1?\d?\d|2[0-4]\d|25[0-5])(?:\.(?:1?\d?\d|2[0-4]\d|25[0-5])){3}(?=$|[^\w.])')
    ipv6regex = r'''(?:^|(?<=\s))(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))(?=\s|$)'''    
    ret = text
    if("--ipv4" in secondary_args and "--ipv6" in secondary_args):
        tmp = re.sub(ipv4_regex, Fore.RED + r'\g<0>' + Fore.RESET, text)
        ret = re.sub(ipv6regex,Fore.RED + r'\1' + Fore.RESET, tmp)
    elif("--ipv4" in secondary_args and "--ipv6" not in secondary_args):
        ret = re.sub(ipv4_regex, Fore.RED + r'\g<0> ' + Fore.RESET, text)
    elif("--ipv4" not in secondary_args and "--ipv6" in secondary_args):
        ret = re.sub(ipv6regex,Fore.RED + r'\1' + Fore.RESET, text)

    return ret

def arguments_handler(used_args):
    target_args = ["--first","--last","--timestamps","--ipv4","--ipv6","-i","-t","-f","-l","-I"]
    priority_args = []
    secondary_args = []
    for arg in target_args:
        if(arg in used_args and arg == "--first" or arg in used_args and arg == "-f"):
            priority_args.append(arg)
        elif(arg in used_args and arg == "--last" or arg in used_args and arg == "-l"):
            priority_args.append(arg)
        elif(arg in used_args and arg == "--timestamps" or arg in used_args and arg == "-t"):
            secondary_args.append(arg)
        elif(arg in used_args and arg == "--ipv4" or arg in used_args and arg == "-i"):
            secondary_args.append(arg)
        elif(arg in used_args and arg == "--ipv6" or arg in used_args and arg == "-I"):
            secondary_args.append(arg)
        else:
            pass
    return priority_args,secondary_args

def stdinput_check():
    stdinput_flag = 0
    if select.select([sys.stdin,],[],[],0.0)[0]:
        stdinput_flag = 1
    return stdinput_flag

def is_argument_set(arg_name):
    if arg_name in sys.argv:
        return True 
    return False

def check_parser_arguments():
    target_args = ["--first","--last","--timestamps","--ipv4","--ipv6","-i","-t","-f","-l","-I"]
    intersected_args = []
    for arg in target_args:
        if(is_argument_set(arg) == True):
            intersected_args.append(arg)
    return intersected_args
    

if __name__ == "__main__":
    parser = ThrowingArgumentParser()
    parser = argparse.ArgumentParser(description='Welcome to log parsing utility v1.02, a Python CLI application that will help you parse logs of various kinds.\n\n\nIf FILE is omitted, standard input is used instead.\nIf multiple options are used at once, the result is the intersection of their results.\nExample supported usage:\n------------------------\n./util.py -h\n<prints help>\n\ncat test_0.log | ./util.py --first 10\n<prints the first 10 lines of test_0.log>\n\n./utils.py --timestamps test_2.log\n<prints any lines from test_2.log that contain a timestamp>\n\n',formatter_class=RawTextHelpFormatter)
    parser.add_argument('-f',"--first",action='store',required=False,default=None, help="Print first NUM lines")
    parser.add_argument('-l',"--last",action='store',required=False,default=None, help="Print last NUM lines")
    parser.add_argument('-t',"--timestamps",action='store_true',required=False,default=None, help="Print lines that contain a timestamp in HH:MM:SS format")
    parser.add_argument('-i',"--ipv4",action='store_true',required=False,default=None, help="Print lines that contain an IPv4 address, matching IPs are highlighted")
    parser.add_argument('-I',"--ipv6",action='store_true',required=False,default=None, help="Print lines that contain an IPv6 address, matching IPs are highlighted")
    parser.add_argument("file",action='store',nargs='?',default=1, type=argparse.FileType('r'), help="Specify a file <filename>.log")

    args, unknown = parser.parse_known_args()
    
    stdin_flag = stdinput_check()

    used_args = check_parser_arguments()

    if(stdin_flag == 1 and args.file == 1):
        #Here we work with the stdin text
        input_text = sys.stdin.readlines()
        args_check = arguments_handler(used_args)
        primary_args_tmp = args_check[0]
        secondary_args_tmp = args_check[1]
        primary_args = check_primary_args(primary_args_tmp)
        secondary_args = check_secondary_args(secondary_args_tmp)
        
        if(len(primary_args) != 0):
            text_to_pass = primary_args_handler(input_text,primary_args)
            if(len(secondary_args) == 0):
                print(text_to_pass)
            else:
                text_to_print = secondary_args_handler(text_to_pass,secondary_args)
                if(text_to_print != ""):
                    print(text_to_print.rstrip())
                else:
                    print("No matches :(")
        else:
            if(len(secondary_args) == 0):
                print("Bad usage. Need to specify an options.\n")
                parser.print_help()
                exit(1)
            else:
                text_to_print = secondary_args_handler(''.join(input_text),secondary_args)
                if(text_to_print != ""):
                    print(text_to_print.rstrip())
                else:
                    print("No matches :(")
    elif(stdin_flag == 0 and args.file != 1):
        with open(args.file.name, 'r') as f:
            file_text = f.readlines()
        #Here we work with the file specified as positional argument 
        args_check2 = arguments_handler(used_args)
        primary_args2_tmp = args_check2[0]
        secondary_args2_tmp = args_check2[1]
        primary_args2 = check_primary_args(primary_args2_tmp)
        secondary_args2 = check_secondary_args(secondary_args2_tmp)

        #         primary_args_tmp = args_check[0]
        # secondary_args_tmp = args_check[1]
        # primary_args = check_primary_args(primary_args_tmp)
        # # secondary_args = check_secondary_args(secondary_args_tmp)

        if(len(primary_args2) != 0):
            text_to_pass2 = primary_args_handler(file_text,primary_args2)
            if(len(secondary_args2) == 0):
                print(text_to_pass2.rstrip())
            else:
                text_to_print2 = secondary_args_handler(text_to_pass2,secondary_args2)
                if(text_to_print2 != ""):
                    print(text_to_print2.rstrip())
                else:
                    print("No matches :(")
        else:
            if(len(secondary_args2) == 0):
                print("Bad usage. Need to specify an options.\n")
                parser.print_help()
                exit(1)
            else:
                text_to_print2 = secondary_args_handler(''.join(file_text),secondary_args2)
                if(text_to_print2 != ""):
                    print(text_to_print2.rstrip())
                else:
                    print("No matches :(")
                
    elif(stdin_flag == 0 and args.file == 1):
        print("Bad usage: please specify <filename.log> or use STDIN to cli.py\n")
        parser.print_help()
        exit(1)
    else:
        print("Bad usage: please specify <filename.log> or use STDIN to cli.py\n")
        #parser.print_help()
        exit(1)

# %%