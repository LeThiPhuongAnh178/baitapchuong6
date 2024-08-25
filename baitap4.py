# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:24:05 2024

@author: Student
"""

time = input("Nhap vao gio, phut va giay (Theo dinh dang hh:mm:ss): ")
hh, mm, ss = map(int, time. split(":"))
if 0 <= hh < 24 and 0 <= mm < 60 and 0 <= ss < 60:
    Doi = hh*3600 + mm*60 + ss
    print("So giay la: ", Doi)
else:
    print("Gio, phut va giay chua hop le")
    