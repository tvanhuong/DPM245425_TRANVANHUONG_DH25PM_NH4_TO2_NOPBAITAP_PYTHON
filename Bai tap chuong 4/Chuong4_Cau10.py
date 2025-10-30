import time
import os
import platform

def clear_screen():
    # Xóa màn hình tương ứng với OS
    if platform.system().lower().startswith("win"):
        os.system("cls")
    else:
        os.system("clear")

# 4 hình mẫu (mỗi hình là một list các dòng)
hinh1 = [
    "    *",
    "    * *",
    "    * * *",
    "* * * * * *",
    "* * * ",
    "* * ",
    "*"
]

hinh2 = [
    "  ***     ***  ",
    " *****   ***** ",
    "******* *******",
    " ************* ",
    "  ***********  ",
    "   *********   ",
    "    *******    ",
    "     *****     ",
    "      ***      ",
    "       *       "








]

hinh3 = [
    "      *",
    "     * *",
    "    *   *",
    "   *     *",
    "  *       *",
    " *         *",
    "* * * * * * *"
]

hinh4 = [
    "*       *",
    " *     * ",
    "  *   *  ",
    "   * *   ",
    "    *    ",
    "   * *   ",
    "  *   *  ",
    " *     * ",
    "*       *"
]

# Danh sách các hình để duyệt
cac_hinh = [hinh1, hinh2, hinh3, hinh4]

# Thời gian chờ (giây)
THOI_GIAN_CHO = 5

def hien_hinh(hinh):
    clear_screen()
    print("\n".join(hinh))

def main():
    for i, h in enumerate(cac_hinh, start=1):
        hien_hinh(h)
        print(f"\n(Hình {i} — sẽ chuyển sau {THOI_GIAN_CHO} giây...)")
        time.sleep(THOI_GIAN_CHO)
    clear_screen()
    print("Đã hiển thị xong 4 hình.")

if __name__ == "__main__":
    main()
