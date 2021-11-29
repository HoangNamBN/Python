def Bai35():
    while True:
        try:
            n = int(input("Nhập số phần tử trong mảng: "))
            if n < 0:
                print("Vui lòng nhập lại số phần tử")
                continue
            else:
                a = []
                for i in range(n):
                    a.append(input("a[" + str(i) + "] = "))
                print("Mảng sau khi nhập là: ", a)
                max = a[0]
                for i in range(1, n):
                    if a[i] > max:
                        max = a[i]
                print("Max = ", max)

        except:
            print("Phải nhập số tự nhiên !")
            continue
        else:
            break
if __name__ == "__main__":
    Bai35()