import numpy
def Bai46():
    while True:
        try:
            m = int(input("Nhập m = "))
            n = int(input("Nhập n = "))
            if n < 0 or m < 0:
                print("Vui lòng nhập lại số phần tử")
                continue
            else:
                a = numpy.zeros((m, n))
                for i in range(m):
                    for j in range(n):
                        a[i][j] = int(input("a[" + str(i) + "][" + str(j)+"]= "))
                print("Ma trận sau khi nhập là:\n", a)
                tong = 0
                
                for i in range(0, m):
                    for j in range(0, n):
                        tong += a[i][j]
                print("Tổng các phần tử trong ma trận: ", tong)

        except:
            print("Phải nhập số tự nhiên !")
            continue
        else:
            break
if __name__ == "__main__":
    Bai46()