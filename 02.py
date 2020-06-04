x = 'パトカー'
y = 'タクシー'

str = ''

for s1, s2 in zip(x , y):
    str += s1 + s2

print(str)