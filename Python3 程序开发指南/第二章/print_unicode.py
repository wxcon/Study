'''
@File    :   print_unicode.py
@Time    :   2021/03/26 13:31:10
@Author  :   mike.wu 
@Version :   0.99
@Contact :   xcwu@whu.edu.cn
'''

#Description: P71 例子 
import sys 
import unicodedata

def print_unicode_table(word): 
    print("decimal    hex   chr   {0:^40}".format("name"))
    print("------- ----- --- {0:-<40}".format(""))
    
    code = ord(" ")
    end = sys.maxunicode 

    while code < end: 
        c = chr(code) 
        name = unicodedata.name(c, "*** unknown ***")
        try:
            if word is None or word in name.lower(): 
                print("{0:7} {0:5x} {0:^3c} {1}".format(code, name.title()))
        except UnicodeEncodeError as err:
            print(err)
            continue
        finally:
            code += 1
word = None 
if len(sys.argv) > 1: 
    if sys.argv[1] in ('-h', '--help'): 
        print('usage: {0} [string]'.format(sys.argv[0]))
        word = 0 
    else:
        word = sys.argv[1].lower()

if word != 0:
    print_unicode_table(word)
