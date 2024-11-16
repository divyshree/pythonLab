""""Pattern #6: Reverse Pyramid of Numbers
Pattern:
     1 
    2 1 
   3 2 1 
  4 3 2 1 
 5 4 3 2 1"""
# Answer to Pattern #6
for i in range(1, 6):
    print(" " * (5 - i) + " ".join(str(x) for x in range(i, 0, -1)))


# Name -> Divyshree Saxena
# 3rd Sem ,Section K
# 23FE10CSE00484