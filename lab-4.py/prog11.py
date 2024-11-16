""""Pattern #11: Connected Inverted Pyramid Pattern of Numbers
Pattern:
5 4 3 2 1 1 2 3 4 5 
5 4 3 2 2 3 4 5 
5 4 3 3 4 5 
5 4 4 5 
5 5"""
# Answer to Pattern #11
for i in range(5, 0, -1):
    row = list(range(5, i - 1, -1)) + list(range(i, 6))
    print(" ".join(str(x) for x in row))