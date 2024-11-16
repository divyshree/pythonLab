""""Pattern #3: Half Pyramid Pattern of Numbers
Pattern:
     1 
    1 2 
   1 2 3 
  1 2 3 4 
 1 2 3 4 5"""
# Answer to Pattern #3
for i in range(1, 6):
    print(" " * (5 - i) + " ".join(str(x) for x in range(1, i + 1)))

# Name -> Divyshree Saxena
# 3rd Sem ,Section K
# 23FE10CSE00484