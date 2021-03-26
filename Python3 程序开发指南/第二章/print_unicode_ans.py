'''
@File    :   print_unicode_ans.py
@Time    :   2021/03/26 16:25:22
@Author  :   mike.wu 
@Version :   0.99
@Contact :   xcwu@whu.edu.cn
'''

#Description: P84 练习题1

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
            flag = True
            for word in words:
                if word not in name.lower():
                    flag = False 
                    break 
            if flag:
                print("{0:7} {0:5x} {0:^3c} {1}".format(code, name.title()))
            code += 1
            
        except UnicodeEncodeError as err:
            print(err)
            continue
        finally:
            code += 1

words = []
if len(sys.argv) > 1: 
    if '-h' in sys.argv or '--help' in sys.argv:
        print('usage: {0} [strings]'.format(sys.argv[0]))
        words = None 
    else:
        for word in sys.argv[1:]:
            words.append(word.lower())

if words is not None: 
    print_unicode_table(words)
