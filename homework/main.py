def SumNguoc():
    while True:
        n = int(input("Nhập số nguyên n: "))
        try:
            if (n <= 0):
                print("Vui lòng nhập lại thỏa mãn điều kiện")
                continue;
            else:
                sum = 0
                for i in reversed(range(1, n+1)):
                    sum += i
                print("Tổng từ 1 đến n là : ", sum)
        except:
            print("Đầu vào không hợp lệ")
            continue;
        else:
            break

if __name__ == "__main__":
    SumNguoc()