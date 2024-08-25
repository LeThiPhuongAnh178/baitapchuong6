# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:40:56 2024

@author: Student
"""

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

#Kiểm tra trường hợp chia cho 0
if b == 0:
    print("Không thể chia cho 0!")
else:
    tong = a+b
    hieu = a-b
    tich = a*b
    thuong_thuc = a/b
    thuong_nguyen = a//b
    du = a%b
#In kết quả ra màn hình  
print("Tong: ", tong)
print("Hieu: ", hieu)
print("Tich: ", tich)
print("Thuong (so thuc):", round(thuong_thuc, 3))
print("Thuong (so nguyen)):", thuong_nguyen)
print("So du:", du)