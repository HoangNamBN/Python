def Giaithua():
    while True:
        n = int(input("Nhập số nguyên n: "))
        try:
            if (n < 0):
                print("Vui lòng nhập số nguyên")
                continue;
            else:
                giaithua = 1
                for i in range(1, n + 1):
                    giaithua *= i
                print(giaithua)
        except:
            print("Đầu vào không hợp lệ")
            continue;
        else:
            break


if __name__ == "__main__":
    Giaithua()
