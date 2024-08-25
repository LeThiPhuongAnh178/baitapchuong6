# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:28:32 2024

@author: Student
"""

import math
a=int(input("nhập số a: "))
b=int(input("nhập số b: "))
A=math.sqrt(a)-math.sqrt(b)
B=math.sqrt(math.sqrt(a))-math.sqrt(math.sqrt(b))
C=math.sqrt(a)+math.sqrt(math.sqrt(a*b))
D=math.sqrt(math.sqrt(a))+math.sqrt(math.sqrt(b))
print("giá trị biểu thức", (A/B)-(C/D))

