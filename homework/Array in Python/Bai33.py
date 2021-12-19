def Bai33():
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
                x = int(input("nhập giá trị cần chèn vào trong mảng: "))
                k = int(input("Nhập vị trí cần chèn: "))
                a.insert(k, x)
                print("Mảng sau khi thêm là", a)
        except:
            print("Phải nhập số tự nhiên !")
            continue
        else:
            break
if __name__ == "__main__":
    Bai33()