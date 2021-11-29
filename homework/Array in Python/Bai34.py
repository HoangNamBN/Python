def Bai34():
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
                a.sort()
                print("Mảng sau khi được sắp xếp tăng dần là: ", a)

        except:
            print("Phải nhập số tự nhiên !")
            continue
        else:
            break
if __name__ == "__main__":
    Bai34()