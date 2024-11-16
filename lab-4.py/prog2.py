""""Pattern #2: Inverted Pyramid of Numbers
Pattern:
1 1 1 1 1 
 2 2 2 2 
  3 3 3 
   4 4 
    5"""
# Answer to Pattern #2
for i in range(5, 0, -1):
    print(" " * (5 - i) + (str(i) + " ") * i)