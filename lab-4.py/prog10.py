""""Pattern #10: Unique Pyramid Pattern of Digits
Pattern:
1 
1 2 1 
1 2 3 2 1 
1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1"""
# Answer to Pattern #10
for i in range(1, 6):
    row = list(range(1, i + 1)) + list(range(i - 1, 0, -1))
    print(" ".join(str(x) for x in row))


# Name -> Divyshree Saxena
# 3rd Sem ,Section K
# 23FE10CSE00484