def Bai26():
    while True:
        result = ""
        n = int(input("Nhập số nguyên n: "))
        try:
            if (n <= 0):
                print("Vui lòng nhập lại thỏa mãn điều kiện")
                continue;
            else:
                a = 1
                b = 1
                for i in range(1, n + 1):
                    if i == 1 or i == 2:
                        result += "1" + " "
                    else:
                        c = a + b
                        result += str(c) + " "
                        a = b
                        b = c
                print(result)
        except:
            print("Đầu vào không hợp lệ")
            continue;
        else:
            break


if __name__ == "__main__":
    Bai26()