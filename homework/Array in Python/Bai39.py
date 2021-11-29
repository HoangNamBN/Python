import math


def Bai39():
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
                for i in range(0, n):
                    if a[i] >0:
                        SL_uoc = 0
                        for j in range(2, a[i]):
                            if a[i]%j == 0:
                                SL_uoc += 1
                        if SL_uoc == 0:
                            dem += 1
                            result += str(a[i]) + " "
                print("Các số nguyên tố trong dãy số là: ", result)
                print("Số lượng số nguyên tố là: ", dem)
        except:
            print("Phải nhập số tự nhiên !")
            continue
        else:
            break


if __name__ == "__main__":
    Bai39()
