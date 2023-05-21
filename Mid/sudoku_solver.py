def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    number_possibilites =  [[[],[],[],[],[],[],[],[],[]],
                            [[],[],[],[],[],[],[],[],[]],
                            [[],[],[],[],[],[],[],[],[]],
                            [[],[],[],[],[],[],[],[],[]],
                            [[],[],[],[],[],[],[],[],[]],
                            [[],[],[],[],[],[],[],[],[]],
                            [[],[],[],[],[],[],[],[],[]],
                            [[],[],[],[],[],[],[],[],[]],
                            [[],[],[],[],[],[],[],[],[]]]


    array_vertical_line = []


    
    return puzzle


def checkSquare(array, array_square):
    square_numbers = [[[],[],[]]
                      [[],[],[]]
                      [[],[],[]]]
    square_i, square_j = 0
    vertical_i, vertical_j = 0, 3
    chorizontal_k, chorizont_l = 0, 3
    while vertical_j < 10:
        while chorizontal_l < 10:
            for vertical in range(vertical_i, vertical_j):
                for chorizontal in range (chorizontal_k, chorizontal_l):
                    array_square[square_i][square_j]
                k, l = 0, 3