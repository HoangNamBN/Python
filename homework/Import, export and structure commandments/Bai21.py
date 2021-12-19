def Bai21():
    while True:
        n = int(input("Nhập số nguyên n: "))
        try:
            if (n <= 0):
                print("Vui lòng nhập lại thỏa mãn điều kiện")
                continue;
            else:
                f = 0
                k = -1
                for i in range(1, n+1):
                    k = k * (-1)
                    f = f + k * i
                print("f (", n, ") = ", f)
        except:
            print("Đầu vào không hợp lệ")
            continue;
        else:
            break


if __name__ == "__main__":
    Bai21()