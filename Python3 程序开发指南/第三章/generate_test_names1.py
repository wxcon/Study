#!/usr/bin/env python3
'''
@File    :   generate_test_names1.py
@Time    :   2021/03/30 15:59:46
@Author  :   mike.wu 
@Contact :   wuxiaoco@gmail.com
'''

import random 

def get_forenames_and_surnames():
    forenames = []
    surnames = []
    for names, filename in ((forenames, './forenames.txt'), (surnames, './surnames.txt')):
        for name in open(filename, encoding="utf8"): 
            names.append(name.rstrip())
    return forenames, surnames

forenames, surnames = get_forenames_and_surnames()
fh = open("test-names1.txt", "w", encoding="utf8")
for i in range(100): 
    line = "{0} {1}\n".format(random.choice(forenames), random.choice(surnames))
    fh.write(line)