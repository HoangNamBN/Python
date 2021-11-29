def Bai14():
    while True:
        n = int(input("Nhập số nguyên n: "))
        try:
            if (n <= 99 or n >=1000):
                print("Vui lòng nhập lại thỏa mãn điều kiện")
                continue;
            else:
                tong = 0
                while n != 0:
                    a = n%10
                    n = n/10
                    tong += a*a*a
                print("Tong = ", tong)
        except:
            print("Đầu vào không hợp lệ")
            continue;
        else:
            break

if __name__ == "__main__":
    Bai14()