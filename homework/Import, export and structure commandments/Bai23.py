def Bai23():
    while True:
        n = int(input("Nhập số nguyên n: "))
        try:
            if (n < 0 or n > 9):
                print("Vui lòng nhập lại thỏa mãn điều kiện")
                continue;
            else:
                result = switchCase(n)
                print(result)
        except:
            print("Đầu vào không hợp lệ")
            continue;
        else:
            break

def switchCase(n):
    switcher = {
        0: 'Zero',
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine'
    }
    return switcher.get(n, "Không hợp lệ!")

if __name__ == "__main__":
    Bai23()