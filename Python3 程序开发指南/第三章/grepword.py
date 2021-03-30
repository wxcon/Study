#!/usr/bin/env python3
'''
@File    :   grepword.py
@Time    :   2021/03/30 15:53:49
@Author  :   mike.wu 
@Contact :   wuxiaoco@gmail.com
'''

import sys 

if len(sys.argv) < 3:
    print("usage: grepword.py word infile1 [infile2 [... infileN]]")
    sys.exit()

word = sys.argv[1]
for filename in sys.argv[2:]: 
    for lino, line in enumerate(open(filename), start = 1):
        if word in line: 
            print("{0}:{1}:{2:.70}".format(filename, lino, line.rstrip()))