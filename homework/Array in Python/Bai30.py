def Bai30():
    while True:
        try:
            n = int(input("Nhập số phần tử trong mảng: "))
            if n < 0:
                print("Vui lòng nhập lại số phần tử")
                continue
            else:
                a = []
                for i in range(n):
                    a.append(int(input("a[" + str(i) + "] = ")))
                print("Mảng sau khi nhập là: ", a)
                tong = 0
                dem = 0
                for i in range(0, n, 2):
                    if a[i]%2 == 1:
                        tong += a[i]
                        dem +=1
                if dem > 0:
                    TBC = float(tong/dem)
                    print("TBC = ", TBC)
                else:
                    print("Không có phần tử lẻ ở vị trí chẵn")
        except:
            print("Phải nhập số tự nhiên !")
            continue
        else:
            break
if __name__ == "__main__":
    Bai30()