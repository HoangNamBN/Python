import numpy
def Bai44():
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
                # cả 2 cách đều cho ra cùng 1 kết quả
                print("Ma trận chuyển vị là :\n", a.T)
                print("Ma trận chuyển vị là :\n", numpy.transpose(a))

        except:
            print("Phải nhập số tự nhiên !")
            continue
        else:
            break
if __name__ == "__main__":
    Bai44()
