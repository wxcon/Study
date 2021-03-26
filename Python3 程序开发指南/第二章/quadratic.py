'''
@File    :   quadratic.py
@Time    :   2021/03/26 15:12:57
@Author  :   mike.wu 
@Version :   0.99
@Contact :   xcwu@whu.edu.cn
'''

#Description: P76例子

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

equation = ("{0}x\N{SUPERSCRIPT TWO} + {1}x + {2} = 0 \N{RIGHTWARDS ARROW} X = {3}").format(a, b, c, x1)
if x2 is not None: 
    equation += " or x = {0}".format(x2)

print(equation)
