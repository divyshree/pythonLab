""""Pattern #9: Reverse Pattern of Digits from 10
Pattern:
1
3 2
6 5 4
10 9 8 7"""
# Answer to Pattern #9
num = 1
for i in range(1, 5):
    row = [str(num + x) for x in range(i)]
    print(" ".join(row[::-1]))
    num += i



# Name -> Divyshree Saxena
# 3rd Sem ,Section K
# 23FE10CSE00484