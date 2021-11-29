s = str(input("Nhập vào xâu s: "))
if len(s) == 0:
    print("Xâu là xâu rỗng!")
else:
    dem = 0
    for i in range(len(s)):
        if s[i] == 'a':
            dem += 1
    print("Số lượng ký tự a trong xâu s là: ", dem)
