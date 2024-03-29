# Author: Brandi Fletcher
# Section: CIS 225 01 
# Date: 10/19/23
# File: friendly.py
#
# Create a program displaying a seating chart for AA
excluded_row = (5, 6, 13, 14)
num_col = 4
seat_col = 'A'
seat_row = 1
def main():
    for curr_row in range(1, 25):
        if curr_row in excluded_row:
            #print('excluded')
            curr_row += 1
            continue
        for i in range(num_col):
            curr_col = 'A'
            print(f'{curr_row}{seat_col}')
            curr_row += 1
        
        
        

main()
