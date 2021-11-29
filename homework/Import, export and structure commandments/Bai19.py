def Bai19():
    while True:
        n = int(input("Nhập số nguyên n: "))
        try:
            if (n <= 0):
                print("Vui lòng nhập lại thỏa mãn điều kiện")
                continue;
            else:
                for i in range(1, n+1):
                    SL_Uoc = 0
                    for j in range(2, i):
                        if i%j == 0:
                            SL_Uoc += 1
                    if SL_Uoc == 0:
                        print(i, " ")
        except:
            print("Đầu vào không hợp lệ")
            continue;
        else:
            break


if __name__ == "__main__":
    Bai19()