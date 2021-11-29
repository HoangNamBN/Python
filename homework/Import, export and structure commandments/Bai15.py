def Bai15():
    while True:
        n = int(input("Nhập số nguyên n: "))
        try:
            if (n <= 100):
                print("Vui lòng nhập lại thỏa mãn điều kiện")
                continue;
            else:
                n_dao = 0
                while n != 0:
                    du = int(n % 10)
                    n_dao = (n_dao * 10) + du
                    n = int(n / 10)
                print("Số đảo: ", int(n_dao))
        except:
            print("Đầu vào không hợp lệ")
            continue;
        else:
            break


if __name__ == "__main__":
    Bai15()
