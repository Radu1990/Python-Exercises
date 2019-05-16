# THIS PROGRAM DRAWS A GRID WITH BASIC FEATURES

# ROW PART


def draw_row_line():
    fre = '+ - - - -'  # first row line element
    print(fre, end=' ')


# Here we define how long the row line length will be.
# Every function defines one column
def draw_row_line_length():
    draw_row_line(), draw_row_line(), draw_row_line(), draw_row_line()


def draw_row_end_point():
    # here we define the row end point
    rep = '+'
    print(rep)


# COLUMN PART
def draw_column():
    # column element
    ce = '|        '
    print(ce, end=' ')


#  here we define how long the column line will be.
#  Every function defines one column
def draw_column_length():
    draw_column(), draw_column(), draw_column(), draw_column()


def draw_column_end_point():
    cep = "|"  # here we define the column end point
    print(cep)


# Reusing functions to draw the grid
# 1
draw_row_line_length(), draw_row_end_point()

draw_column_length(), draw_column_end_point() 
draw_column_length(), draw_column_end_point()
draw_column_length(), draw_column_end_point()
draw_column_length(), draw_column_end_point()

# 2
draw_row_line_length(), draw_row_end_point()

draw_column_length(), draw_column_end_point()
draw_column_length(), draw_column_end_point()
draw_column_length(), draw_column_end_point()
draw_column_length(), draw_column_end_point()

# 3
draw_row_line_length(), draw_row_end_point()

draw_column_length(), draw_column_end_point()
draw_column_length(), draw_column_end_point()
draw_column_length(), draw_column_end_point()
draw_column_length(), draw_column_end_point()

# 4
draw_row_line_length(), draw_row_end_point()

draw_column_length(), draw_column_end_point()
draw_column_length(), draw_column_end_point()
draw_column_length(), draw_column_end_point()
draw_column_length(), draw_column_end_point()

# 5 end
draw_row_line_length(), draw_row_end_point()
