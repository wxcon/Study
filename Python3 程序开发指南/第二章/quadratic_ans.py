'''
@File    :   quadratic_ans.py
@Time    :   2021/03/26 17:14:49
@Author  :   mike.wu 
@Version :   0.99
@Contact :   xcwu@whu.edu.cn
'''

#Description: P84 练习题2 

import cmath 
import math 
import sys 

def get_float(msg, allow_zero): 
    x = None 
    while x is None: 
        try: 
            x = float(input(msg))
            if not allow_zero and abs(x) < sys.float_info.epsilon: 
                print("zeron is not allowrd")
                x = None 
        except ValueError as err:
            print(err)
        return x 
    
print("ax\N{SUPERSCRIPT TWO} + bx + c = 0")
a = get_float("enter a: ", False)
b = get_float("enter b: ", True)
c = get_float("enter c: ", True)

x1 = None 
x2 = None 
discriminat = (b **2) - (4 * a * c)
if discriminat == 0: 
    x1 = -(b / (2 * a))
else: 
    if discriminat > 0: 
        root = math.sqrt(discriminat)
    else: 
        root = cmath.sqrt(discriminat)
    x1 = (-b + root) / (2 * a)
    x2 = (-b - root) / (2 * a)


equation = ("{0}x\N{SUPERSCRIPT TWO}").format(a)
if b > 0:
    equation += " + {0}x".format(b)
else:
    equation += " - {0}x".format(-b)

if c > 0:
    equation += " + {0} = 0".format(c)
else:
    equation += " - {0} = 0".format(-c)

if b == 0 or c == 0:
    pass 
else:
    equation += " \N{RIGHTWARDS ARROW} X = {0}".format(x1)
    if x2 is not None: 
        equation += " or x = {0}".format(x2)
    print(equation)
