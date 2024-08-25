# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 16:20:00 2024

@author: Student
"""

# Chuỗi địa chỉ
dia_chi = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"

# 1. Tách thành các sub-string theo dấu phẩy và dấu cách
sub_strings_1 = dia_chi.split(", ")

# 2. Tách thành các sub-string và loại bỏ "P.", "Q.", "Tp."
sub_strings_2 = []
for sub in sub_strings_1:
    if "P." in sub:
        sub_strings_2.append(sub[2:])
    elif "Q." in sub:
        sub_strings_2.append(sub[2:])
    elif "Tp." in sub:
        sub_strings_2.append(sub[3:])
    else:
        sub_strings_2.append(sub)

# In kết quả
print("Kết quả 1:")
for sub in sub_strings_1:
    print(sub)

print("\nKết quả 2:")
for sub in sub_strings_2:
    print(sub)