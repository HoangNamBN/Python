def Bai25():
    while True:
        result = ""
        n = int(input("Nhập số nguyên n: "))
        try:
            if (n <= 0):
                print("Vui lòng nhập lại thỏa mãn điều kiện")
                continue;
            else:
                for i in range(1, n*n + 1):
                    result += str(i) + " "
                    if i % n == 0:
                        result += "\n"
                print(result)
        except:
            print("Đầu vào không hợp lệ")
            continue;
        else:
            break


if __name__ == "__main__":
    Bai25()