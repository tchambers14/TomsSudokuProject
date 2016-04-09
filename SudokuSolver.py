
import numpy

# Program to solve a sudoku

# Ask user to input values in order
# Add optional array of sudoku as inputs
# TODO scrape sudoku from the web to solve


# Define a sudoku grid as an array
grid = numpy.zeros((9,9))

grid[0,0] = 3
grid[0,1] = 8
grid[0,2] = 7
grid[0,4] = 6
grid[0,6] = 9
grid[0,7] = 1
grid[1,2] = 2
grid[1,4] = 5
grid[1,5] = 1
grid[1,8] = 7
grid[2,0] = 5
grid[2,3] = 3
grid[2,4] = 7
grid[2,6] = 2
grid[2,7] = 6
grid[3,2] = 8
grid[3,3] = 5
grid[3,7] = 7
grid[5,1] = 9
grid[5,5] = 6
grid[5,6] = 5
grid[6,1] = 4
grid[6,2] = 6
grid[6,4] = 2
grid[6,5] = 3
grid[6,8] = 1
grid[7,0] = 1
grid[7,3] = 6
grid[7,4] = 9
grid[7,6] = 3
grid[8,1] = 2
grid[8,2] = 3
grid[8,4] = 1
grid[8,6] = 4
grid[8,7] = 9
grid[8,8] = 6

#print grid


# function check if x in row
def element_in_row(number,row):
    if number in grid[row,:]:
        return True
    else:
        return False

# function check if x in column
def element_in_column(number,column):
    if number in grid[: ,column]:
        return True
    else:
        return False

# function check if x in box
def element_in_box(number, row_position, column_position):
    #Determine which box it is in



# numbers = [1,2,3,4,5,6,7,8,9]

#Grid Class
class Sudoku:

    def __init__(self, grid):
        self.grid = np.zeros((9,9,1))
        self.complete = False #Boolean to check if grid is complete
        self.valid = False #Boolean to check if grid is valid


    # function check if x in row
    def element_in_row(number,row):
        if number in grid[row,:]:
            return True
        else:
            return False

    # function check if x in column
    def element_in_column(number,column):
        if number in grid[: ,column]:
            return True
        else:
            return False

    # function check if x in box
    def element_in_box(number, row_position, column_position):
    #Determine which box it is in
    
    # function to print grid
    


        def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2 * self.x + 2 * self.y

    def describe(self, text):
        self.description = text

    def authorName(self, text):
        self.author = text

    def scaleSize(self, scale):
        self.x = self.x * scale
        self.y = self.y * scale