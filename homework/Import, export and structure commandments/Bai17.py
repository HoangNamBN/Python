def Bai17():
    while True:
        n = int(input("Nhập số nguyên n: "))
        try:
            if (n <= 0):
                print("Vui lòng nhập lại thỏa mãn điều kiện")
                continue;
            else:
                GTT = 1
                if n % 2 == 0:
                    for i in range(2, n + 1, 2):
                        GTT *= i
                else:
                    for i in range(1, n + 1, 2):
                        GTT *= i
                print(n, "!! = ", GTT)
        except:
            print("Đầu vào không hợp lệ")
            continue;
        else:
            break


if __name__ == "__main__":
    Bai17()
