import math


def Bai38():
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
                dem = 0
                for i in range(0,n):
                    b = int(math.sqrt(a[i]))
                    if b*b == a[i]:
                        result += str(a[i]) + " "
                        dem += 1
                print("Các số chính phương trong dãy số là: ", result)
                print("Số lượng số chính phương là: ", dem)
        except:
            print("Phải nhập số tự nhiên !")
            continue
        else:
            break
if __name__ == "__main__":
    Bai38()