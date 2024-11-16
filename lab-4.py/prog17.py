""""Pattern #17: Downward Triangle Pattern of Stars
Pattern:
        * * * * * * 
         * * * * * 
          * * * * 
           * * * 
            * * 
             *
"""
# Answer to Pattern #17
for i in range(6, 0, -1):
    print(" " * (6 - i) + "* " * i)