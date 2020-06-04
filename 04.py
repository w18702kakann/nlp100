se = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

words = se.split()

word_list = list(words)

num = {1, 5, 6, 7, 8, 9, 15, 16, 19}
a = {}

num_1 = 0
for i in word_list :
    num_1 += 1
    if num_1 in num :
        fi_i = i[0]
    else :
        fi_i = i[:2]
    a[fi_i] = num_1
print(a)