def Bai32():
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
                for i in range(0, n):
                    if a[i] < 0:
                        for j in range(i, n - 1):
                            a[j] = a[j + 1]
                        n = n - 1
                b = []
                for i in range(0, n):
                    b.append(a[i])
                print("Mảng sau khi xóa phần tử âm là: ", b)
        except:
            print("Phải nhập số tự nhiên !")
            continue
        else:
            break
if __name__ == "__main__":
    Bai32()
