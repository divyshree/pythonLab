""""Pattern #5: Inverted Pyramid of the Same Digit
Pattern:
5 5 5 5 5 
 5 5 5 5 
  5 5 5 
   5 5 
    5"""
# Answer to Pattern #5
for i in range(5, 0, -1):
    print(" " * (5 - i) + (str(5) + " ") * i)