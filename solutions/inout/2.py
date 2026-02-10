k = int(input())
h = (k// 3600) % 24
m = (k % 3600) // 60
s = k - h * 3600 - m *60
print(f'It is {h} hours {m} minutes.')