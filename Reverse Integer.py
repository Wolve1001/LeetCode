class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2147483648, 2147483647 #limits of a 32-bit integer, you would know them as (-2^31, 2^31 - 1)
        y = abs(x) #take absolute value to remove any negative sign
        reversed_x = 0

        while y != 0: 
            pop = y % 10 #get last digit of the number
            y //= 10 #remove last digit of the number
          '''
          y = 123
          1st pass : pop = 3, y = 12 (12.3 but integer division)
          2nd pass : pop = 2, y = 1
          3rd pass : pop = 1, y = 0 {End of loop}
          '''
            if reversed_x > (INT_MAX - pop) / 10: #make sure the value of reversed_x is not overflowing, if so then no need for further calculations
                return 0
            
            reversed_x = reversed_x * 10 + pop #start forming the reversed_x integer
      '''
      1st pass : 0*10 + 3 = 3
      2nd pass : 3*10 + 2 = 32
      3rd pass : 32*10 + 1 = 321
      ''' 
        if x < 0:
            reversed_x = -reversed_x #change to negative if x was negative
        
        if INT_MIN <= reversed_x <= INT_MAX:
            return reversed_x
        else:
            return 0
