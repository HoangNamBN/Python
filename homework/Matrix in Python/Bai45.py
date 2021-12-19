import numpy

def Bai45():
    m = int(input("Nhập m = "))
    n = int(input("Nhập n = "))
    a = numpy.zeros((m, n))
    for i in range(m):
        for j in range(n):
            a[i][j] = int(input("a[" + str(i) + "][" + str(j) + "]= "))
    print("Ma trận thứ 1 là:\n", a)

    print("Nhập ma trận thứ 2: ")
    m1 = int(input("Nhập m1 = "))
    n1 = int(input("Nhập n1 = "))
    b = numpy.zeros((m1, n1))
    for i in range(m1):
        for j in range(n1):
            b[i][j] = int(input("b[" + str(i) + "][" + str(j) + "]= "))
    print("Ma trận thứ 2 là:\n", b)
    print("Tổng hai ma trận là: \n", a + b)


if __name__ == "__main__":
    Bai45()
