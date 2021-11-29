def Bai28():
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
                b = []
                for i in reversed(range(0, n)):
                    b.append(a[i])
                print("Mảng đảo của mảng sau khi nhập là: ", b)

        except:
            print("Phải nhập số tự nhiên !")
            continue
        else:
            break
if __name__ == "__main__":
    Bai28()
