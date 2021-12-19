def Bai41():
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
                x = int(input("nhập giá trị cần tìm trong mảng: "))
                kt = False
                for i in range(0, n):
                    if a[i] == x:
                        kt = True
                        break
                if kt == True:
                    print(x, "tồn tại trong mảng!")
                else:
                    print(x, "không tồn tại trong mảng")
        except:
            print("Phải nhập số tự nhiên !")
            continue
        else:
            break
if __name__ == "__main__":
    Bai41()