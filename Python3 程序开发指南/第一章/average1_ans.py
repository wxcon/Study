'''
@File    :   average1_ans.py
@Time    :   2021/03/25 15:57:41
@Author  :   mike.wu 
@Version :   0.99
@Contact :   xcwu@whu.edu.cn
'''

#Description: P35 第一章练习题2

number_list = []

while True: 
    line = input("enter a number or Enter to finish: ")
    if line: 
        try: 
            number = int(line)
            number_list.append(number)
        except ValueError as err: 
            print(err)
    else: 
        break 

if len(number_list): 
    print("numbers: ", number_list)
    print("count = {} sum = {} lowest = {} highest = {} mean = {:6f}".format(len(number_list), sum(number_list), min(number_list), max(number_list), sum(number_list)/len(number_list)))
    
    
        
        
