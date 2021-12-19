def Bai31():
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
                result = ""
                for i in range(0, n):
                    if a[i] %3 == 0:
                        result += str(i) + " "
                print("Các vị trí của các phần tử chia hết cho 3 là: ", result)
        except:
            print("Phải nhập số tự nhiên !")
            continue
        else:
            break
if __name__ == "__main__":
    Bai31()
