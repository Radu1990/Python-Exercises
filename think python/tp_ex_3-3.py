
# THIS PROGRAM DRAWS A GRID WITH BASIC FEATURES

### ROW PART
def draw_row_line():
    fre = ('+ - - - -') #first row line element
    print(fre, end=' ')
def draw_row_line_length(): #here we define how long the row line length will be / / / every function defines one column
    draw_row_line(), draw_row_line(), draw_row_line(), draw_row_line()
def draw_row_end_point():
    rep = ('+') #here we define the row end point
    print(rep)

### COLUMN PART
def draw_column():
    ce = ('|        ') #column element
    print(ce, end=' ')
def draw_column_length(): #here we define how long the column line will be / / / every function defines one column
    draw_column(), draw_column(), draw_column(), draw_column()
def draw_column_end_point():
    cep = ("|") #here we define the column end point
    print(cep)

#Reusing functions to draw the grid
#1
draw_row_line_length(), draw_row_end_point()

draw_column_length(), draw_column_end_point() 
draw_column_length(), draw_column_end_point()
draw_column_length(), draw_column_end_point()
draw_column_length(), draw_column_end_point()

#2
draw_row_line_length(), draw_row_end_point()

draw_column_length(), draw_column_end_point()
draw_column_length(), draw_column_end_point()
draw_column_length(), draw_column_end_point()
draw_column_length(), draw_column_end_point()

#3
draw_row_line_length(), draw_row_end_point()

draw_column_length(), draw_column_end_point()
draw_column_length(), draw_column_end_point()
draw_column_length(), draw_column_end_point()
draw_column_length(), draw_column_end_point()

#4
draw_row_line_length(), draw_row_end_point()

draw_column_length(), draw_column_end_point()
draw_column_length(), draw_column_end_point()
draw_column_length(), draw_column_end_point()
draw_column_length(), draw_column_end_point()

#5 end
draw_row_line_length(), draw_row_end_point()



