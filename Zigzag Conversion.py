class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s): #edge case if number of rows is just one (one row then) or is greater than the length of the string (one column then)
            return s
        
        rows = [''] * numRows #initialize list with same number of spaces as number of rows given
        current_row = 0
        direction = -1 

        for char in s:
            rows[current_row] += char #we add character to each '' as per the row it should be in
                                                                                                                                      
            if current_row == 0 or current_row == numRows - 1: #once reached the end of the list or the beginning
                direction *= -1 #change direction, -1 goes left, 1 goes right
            current_row += direction #update value of current_row by adding direction
        
        return ''.join(rows) #join all the values in each '' in the list to get the result

  '''
  "PAYPALISHIRING" numRows = 3
   P   A   H   N
   A P L S I I G
   Y   I   R
                                                                                                                            
   P is in the first row, so P will be added to the first ''
   A is in the second row, A will be added to the second ''
                                                                                                                            
  rows = ['PAHN','APLSIIG','YIR'] Final list will look like this for the above example
  '''
