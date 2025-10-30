''' Viết chương trình tính loga
x với a, x là các số thực nhập vào từ bàn phím, và x>0, a>0, a
!= 1.( dùng logax=lnx/lna)
'''
import math
a = float(input("Nhập cơ số a (a > 0, a ≠ 1): "))
x = float(input("Nhập số x (x > 0): "))

# Kiểm tra điều kiện hợp lệ
if a <= 0 or a == 1:
    print("Giá trị của a không hợp lệ! (phải có a > 0 và a ≠ 1)")
elif x <= 0:
    print("Giá trị của x không hợp lệ! (phải có x > 0)")
else:
    loga_x = math.log(x) / math.log(a)
    print(f"log_{a}({x}) = {loga_x:.2f}")