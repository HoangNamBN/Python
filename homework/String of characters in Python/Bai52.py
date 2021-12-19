s = str(input("Nhập vào xâu kí tự s: "))
if len(s) == 0:
    print("Xâu là xâu rỗng!")
else:
    print("Xâu đảo của xâu kí tự ", s, "là", ''.join(reversed(s)))
