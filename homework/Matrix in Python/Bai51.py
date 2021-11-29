import numpy

def Bai51():
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
                dem = 0
                for i in range(0, n):
                    for j in range(0, n):
                        if a[i][j]%2 == 0:
                            dem += 1
                print("Số lượng số chẵn trong ma trận là: ", dem)


        except:
            print("Phải nhập số tự nhiên !")
            continue
        else:
            break

if __name__ == "__main__":
    Bai51()