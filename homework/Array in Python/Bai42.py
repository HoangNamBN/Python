def Bai42():
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
                kt = True
                for i in range(1, n):
                    if a[i] < a[i - 1]:
                        kt = False
                        break
                if kt == True:
                    print("Mảng được sắp xếp tăng dần!")
                else:
                    print("Mảng không được sắp xếp tăng dần")
        except:
            print("Phải nhập số tự nhiên !")
            continue
        else:
            break
if __name__ == "__main__":
    Bai42()