def Bai29():
    while True:
        try:
            n = int(input("Nhập số phần tử trong mảng: "))
            if n < 0:
                print("Vui lòng nhập lại số phần tử")
                continue
            else:
                a = []
                for i in range(n):
                    a.append(float(input("a[" + str(i) + "] = ")))
                print("Mảng sau khi nhập là: ", a)
                if n == 0:
                    print("Mảng không có phần tử nào!")
                else:
                    Tong = 0
                    for i in range(0, n):
                        Tong += int(a[i])
                    print("TBC = ", float(Tong/n))

        except:
            print("Phải nhập số tự nhiên !")
            continue
        else:
            break
if __name__ == "__main__":
    Bai29()