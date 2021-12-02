import pandas as pd

dict = {'Tên': 'Long', 'Tuổi': 19, 'Lớp': 'D13CNPM3'}
print(dict)
print(dict['Tên'])
print(dict['Tuổi'])
print(dict['Lớp'])


dic_data = {'Tên': ['Long', 'Đạt', 'Hạnh', 'Toàn'],  # Tên: key , [] - value
            'Lớp': ['D13CNPM3', 'D13CNPM6', 'D13CNPM3', 'D13CNPM5'],
            'Địa chỉ': ['Hà Nội', 'Quảng Ninh', 'Thái Bình', 'Hà Nội'],
            'Điểm': [9, 2, 3, 10]}

for item in dic_data.items():
    print(item)

for key, value in dic_data.items():
    print('key = ', key, ' value = ', value)
    for v in value:
        print(v)


print("================================")
df = pd.DataFrame(dic_data)
print(df)
print(df[['Tên', 'Lớp']])
print(df.iloc[1])
