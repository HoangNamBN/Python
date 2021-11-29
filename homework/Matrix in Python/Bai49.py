import numpy

def Bai49():
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
                result = ""
                for i in range(0, n):
                    result += str(a[i][n-i-1]) + ", "
                print("Các phần tử thuộc đường chéo phụ: ", result)

        except:
            print("Phải nhập số tự nhiên !")
            continue
        else:
            break


if __name__ == "__main__":
    Bai49()