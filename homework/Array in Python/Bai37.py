def Bai37():
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
                Tich = 1
                for i in range(0,n):
                    if a[i] > 0:
                        Tich *= a[i]
                print("Tích các số dương: ", Tich)
        except:
            print("Phải nhập số tự nhiên !")
            continue
        else:
            break
if __name__ == "__main__":
    Bai37()
