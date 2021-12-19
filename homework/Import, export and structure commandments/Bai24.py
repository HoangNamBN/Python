def Bai24():
    TDM = 1000
    NDM = 2000
    HGD = 100
    HKD = 250
    HSX = 420
    while True:
        n = int(input("Nhập số nguyên n: "))
        try:
            if (n < 0):
                print("Vui lòng nhập lại thỏa mãn điều kiện")
                continue;
            else:
                print("Nhập loại hộ: \n1. Hộ gia đình\n2. Hộ kinh doanh\n3. Hộ sản xuất\n")
                STT = int(input("Nhập loại hộ: "))
                try:
                    if (STT < 1 or STT > 3):
                        print("Xin vui lòng nhập lại số hộ")
                        continue
                    else:
                        while True:
                            if STT == 1:
                                DM = HGD
                                break
                            elif STT == 2:
                                DM = HKD
                                break
                            else:
                                DM = HSX
                                break
                    if n - DM > 0:
                        SoTien = DM * TDM + (n - DM) * NDM
                    else:
                        SoTien = n * TDM
                    print("Số tiền phải trả là: ", int(SoTien))
                except:
                    print("Đầu vào không hợp lệ")
                    continue;
        except:
            print("Đầu vào không hợp lệ")
            continue;
        else:
            break


if __name__ == "__main__":
    Bai24()
