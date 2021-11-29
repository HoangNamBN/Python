import re

s = str(input("Nhập vào xâu s: "))
if len(s) == 0:
    print("Xâu là xâu rỗng!")
else:
    s = s.strip()
    s = re.sub(r"\s\s+", " ", s)
    dem = 0
    for i in range(len(s)):
        if s[i] == ' ':
            dem += 1
    print("Số lượng từ trong xâu là: ", dem + 1)

