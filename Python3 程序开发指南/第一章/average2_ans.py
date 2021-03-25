'''
@File    :   awfulpoetry2_ans.py
@Time    :   2021/03/25 16:28:51
@Author  :   mike.wu 
@Version :   0.99
@Contact :   xcwu@whu.edu.cn
'''

#Description: P36 第一章练习题4 

import random 

article = ["the", "a"]
title = ["cat", "dog", "man", "woman"]
verb = ["sang", "ran", "jumped"]
adverbial = ["loudly", "quietly", "well", "badly"]

count = 0
number = input("Please input the poetry number: ")

if number:
    try:
        count_value = int(number)
    except ValueError as err:
        print(err)
else: 
    count_value = 5

while count < count_value: 
    line = ""
    line += random.choice(article)+" "
    line += random.choice(title)+" "
    line += random.choice(verb)+" "
    line += random.choice(adverbial)
    print(line)
    count += 1
