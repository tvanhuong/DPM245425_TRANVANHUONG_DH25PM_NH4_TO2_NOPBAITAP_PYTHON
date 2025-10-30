''' Viết chương trình tính căn bậc 2 lồng nhau'''
import math

# Nhập n
n = int(input("Nhập số n (số dấu căn): "))

# Biến lưu kết quả
S = 0

# Tính từ trong ra ngoài
for i in range(n):
    S = math.sqrt(2 + S)

# Xuất kết quả
print(f"S({n}) = {S:.6f}")

