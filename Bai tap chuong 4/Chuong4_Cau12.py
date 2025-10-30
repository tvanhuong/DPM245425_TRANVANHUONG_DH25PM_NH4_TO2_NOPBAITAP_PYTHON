'''  Hàm oscillate 
Hãy viết hàm oscillate để khi chạy phần mềm, nó ra kết quả:
-3 3 -2 2 -1 1 0 0 1 -1 2 -2 3 -3 4 -4'''
def oscillate(a, b):
    for i in range(a, b):
        yield i
        yield -i

# Kiểm tra:
for n in oscillate(-3, 5):
    print(n, end=' ')
