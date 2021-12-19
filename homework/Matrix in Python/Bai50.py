import numpy

def Bai50():
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
                        a[i][j] = int(input("a[" + str(i) + "][" + str(j) + "]= "))
                print("Ma trận sau khi nhập là:\n", a)
                if m < 3:
                    print("Ma trận không có cột 2!")
                else:
                    max = a[2][0]
                    for i in range(1, n):
                        if a[2][i] > max:
                            max = a[2][i]
                    print("Max tại cột 2 là: ", max)

        except:
            print("Phải nhập số tự nhiên !")
            continue
        else:
            break


if __name__ == "__main__":
    Bai50()