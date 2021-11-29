import numpy

def Bai48():
    while True:
        try:
            n = int(input("Nhập n = "))
            if n < 0:
                print("Vui lòng nhập lại số phần tử")
                continue
            else:
                a = numpy.zeros((n, n))
                for i in range(n):
                    for j in range(n):
                        a[i][j] = int(input("a[" + str(i) + "][" + str(j) + "]= "))
                print("Ma trận sau khi nhập là:\n", a)
                tong = 0
                for i in range(0, n):
                    tong += a[i][i]
                print("Tổng đường chéo chính là: ", tong)


        except:
            print("Phải nhập số tự nhiên !")
            continue
        else:
            break

if __name__ == "__main__":
    Bai48()