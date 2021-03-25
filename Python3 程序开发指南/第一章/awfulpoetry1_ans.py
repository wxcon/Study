'''
@File    :   awfulpoetry1_ans.py
@Time    :   2021/03/25 16:15:05
@Author  :   mike.wu 
@Version :   0.99
@Contact :   xcwu@whu.edu.cn
'''

#Description: P36 第一章练习题3 
import random 

article = ["the", "a"]
title = ["cat", "dog", "man", "woman"]
verb = ["sang", "ran", "jumped"]
adverbial = ["loudly", "quietly", "well", "badly"]

count = 0
while count < 5: 
    line = ""
    line += random.choice(article)+" "
    line += random.choice(title)+" "
    line += random.choice(verb)+" "
    line += random.choice(adverbial)
    print(line)
    count += 1
