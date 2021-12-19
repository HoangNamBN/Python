def Bai36():
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
                min = a[0]
                for i in range(0, n):
                    if min > a[i]:
                        min = a[i]
                result = ""
                for i in range(0, n):
                    if a[i] == min:
                        result += str(i) + " "
                print("các vị trí của các phần tử nhỏ nhất là: ", result)

        except:
            print("Phải nhập số tự nhiên !")
            continue
        else:
            break
if __name__ == "__main__":
    Bai36()