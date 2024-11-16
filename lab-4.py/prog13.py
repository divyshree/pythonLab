""""Pattern #13: Pyramid of Horizontal Tables
Pattern:
0  
0 1  
0 2 4  
0 3 6 9  
0 4 8 12 16  
0 5 10 15 20 25  
0 6 12 18 24 30 36"""
# Answer to Pattern #13
for i in range(7):
    print(" ".join(str(i * x) for x in range(i + 1)))


# Name -> Divyshree Saxena
# 3rd Sem ,Section K
# 23FE10CSE00484