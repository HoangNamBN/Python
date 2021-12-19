import math


def Bai40():
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
                        a[i] = 0
                print("Mảng sau khi thay đổi là: ", a)
        except:
            print("Phải nhập số tự nhiên !")
            continue
        else:
            break


if __name__ == "__main__":
    Bai40()
