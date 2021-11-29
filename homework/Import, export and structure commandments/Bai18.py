def Bai18():
    while True:
        n = int(input("Nhập số nguyên n: "))
        try:
            if (n <= 0):
                print("Vui lòng nhập lại thỏa mãn điều kiện")
                continue;
            else:
                SL_Uoc = 0
                for i in range(2, n):
                    if n%i == 0:
                        SL_Uoc += 1
                if SL_Uoc ==0:
                    print(n, "là số nguyên tố!")
                else:
                    print(n, "không là số nguyên tố!")
        except:
            print("Đầu vào không hợp lệ")
            continue;
        else:
            break


if __name__ == "__main__":
    Bai18()