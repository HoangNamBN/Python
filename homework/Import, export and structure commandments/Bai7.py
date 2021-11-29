def Bai7():
    while True:
        try:
            n = int(input("Nhập số nguyên n: "))
            for i in reversed(range(1, n + 1)):
                s = "*"*i
                print(s)
        except ValueError:
            print("Đầu vào không hợp lệ")
            continue;
        else:
            break

if __name__ == "__main__":
    Bai7()
