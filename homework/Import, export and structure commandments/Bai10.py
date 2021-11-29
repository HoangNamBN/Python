def Bai10():
    while True:
        n = int(input("Nhập số nguyên n: "))
        try:
            if (n < 0):
                print("Vui lòng nhập số nguyên")
                continue;
            else:
                dem = 0
                for i in range(1, n + 1):
                    if n%i == 0:
                        dem += 1
                print("Số ước = ", dem)
        except:
            print("Đầu vào không hợp lệ")
            continue;
        else:
            break

if __name__ == "__main__":
    Bai10()