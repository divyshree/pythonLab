""""Pattern #14: Pyramid Pattern of Alternate Numbers
Pattern:
1 
3 3 
5 5 5 
7 7 7 7 
9 9 9 9 9"""
# Answer to Pattern #14
num = 1
for i in range(1, 6):
    print(" ".join([str(num)] * i))
    num += 2