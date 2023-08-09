__author__ = "Johnathan Friend"

import random
import turtle

class Minesweeper:

    def __init__(self, windowLength, windowHeight, width, height, numRows, numColumns,
                 imageList, turtlesList, valuesList, coversList, numBombs, gameOver=False):
        '''
        Object Constructor
        '''
        #variable initialization
        self.windowLength = windowLength
        self.windowHeight = windowHeight
        self.width = width
        self.height = height
        self.numRows = numRows
        self.numColumns = numColumns
        self.imageList = imageList
        self.turtlesList = turtlesList
        self.valuesList = valuesList
        self.coversList = coversList
        self.numBombs = numBombs
        self.gameOver = gameOver

        #adds cover images to covers list
        self.coversList.append('images/a.gif')
        self.coversList.append('images/b.gif')
        self.coversList.append('images/c.gif')

        #registers shape names
        for x in range(13):
            shape_name = 'images/' + str(format(x, "x")) + '.gif'
            self.imageList.append(shape_name)
        

    def createValuesList(self):
        '''
        param: self
        return: None
        creates an empty values list based upon the number of rows and columns for the game
        ''' 

        #adds all 0's to valuesList
        for x in range(self.numRows):
            values_sublist = []
            self.valuesList.append(values_sublist)
            for y in range(self.numColumns):
                values_sublist.append(0)
    
    def startGame(self):
        '''
        param: self
        return: None
        starts the turtle window, sets up the screen and registers the gif images
        '''
        turtle.setup(self.windowLength, self.windowHeight)
        self.win = turtle.Screen()
        self.win.bgcolor("skyblue")

        for x in self.imageList:
            self.win.register_shape(x)
        
        #calls left and right button when clicked
        self.win.onclick(self.leftButtonClick, 1, True)
        self.win.onclick(self.rightButtonClick, 3, True)
    
    def createTurtles(self):
        '''
        param: None
        return: None
        creates the turtle objects and adds to turtle object list
        '''
        for x in range(self.numRows):
            turtles_sublist = []
            self.turtlesList.append(turtles_sublist)
            for y in range(self.numColumns):
                bobTheTurtle = turtle.Turtle()
                turtles_sublist.append(bobTheTurtle)
        
        #hides the turtles and sets their speed to 0
        for x in range(len(self.turtlesList)):
            for y in range(len(self.turtlesList[x])):
                self.turtlesList[x][y].hideturtle()
                self.turtlesList[x][y].speed(0)
        

    def createBombs(self):
        '''
        param: self
        return: none
        determines where the bombs will be located on the grid
        '''
        #gets random locations for the bombs and calls function to update cells
        count = 0
        while count < self.numBombs:
            row_i = random.randint(0, self.numRows-1)
            column_j = random.randint(0, self.numColumns-1)
            if self.valuesList[row_i][column_j] == 9:
                continue
            else:
                self.valuesList[row_i][column_j] = 9
                count += 1
                self.updateNeighbors(row_i, column_j)

    def updateNeighbors(self, row_i, column_j):
        '''
        calls the updateNeighbor function 8 times for the surronding the cells of
        the bombs
        param: int row, int column
        return: None
        '''
        #calls the updateNeighbor functions
        self.updateNeighbor(row_i-1, column_j-1)
        self.updateNeighbor(row_i-1, column_j)
        self.updateNeighbor(row_i-1, column_j+1)
        self.updateNeighbor(row_i, column_j-1)
        self.updateNeighbor(row_i, column_j+1)
        self.updateNeighbor(row_i+1, column_j-1)
        self.updateNeighbor(row_i+1, column_j)
        self.updateNeighbor(row_i+1, column_j+1)
            
    def updateNeighbor(self, row_i, column_j):
        '''
        param: int row, int column
        return: None
        increments the surronding cells of the bombs to adjust to number of
        adjacent bombs
        '''
        if row_i >= 0 and row_i <= (self.numRows-1):
            if column_j >= 0 and column_j <= (self.numColumns-1):
                if self.valuesList[row_i][column_j] != 9:
                    self.valuesList[row_i][column_j] += 1
        
    def drawGrid(self):
        '''
        param: self
        return: none
        draws the minesweeper grid using turtle objects
        '''
        #adds the image to the cells depending on the value of the cell to draw grid
        gridX = (-1 * self.numColumns) * (self.width // 2)
        gridY = (self.numRows * self.height // 2)

        for x in range(self.numRows):
            for y in range(self.numColumns):
                self.turtlesList[x][y].shape(self.imageList[10])
                self.turtlesList[x][y].penup()
                self.turtlesList[x][y].goto(gridX, gridY)
                self.turtlesList[x][y].showturtle()
                gridX += self.width   
            gridY -= self.height
            gridX = -1 * (self.numColumns * self.width // 2)
    
    def revealImage(self, row, column):
        '''
        param: self, row int, column int
        return: none
        takes row and column as parameters and determines which grid cell is revealed
        if user enters a 9/bomb then game ends. If user enters 0 then recursive function
        used and grid is cleared of 0 in area.
        '''

        #determines if the row and column clicked were within bounds
        if row >= 0 and row < self.numRows:
            if column >= 0 and column < self.numColumns:
                if not self.turtlesList[row][column].shape() in self.coversList:
                    return
                else:
                    #adds the image to the cells depending on the value of the cell to draw grid
                    self.turtlesList[row][column].shape(self.imageList[self.valuesList[row][column]])

                    #ends the game if user hits a bomb
                    if self.valuesList[row][column] == 9:
                        self.turtlesList[self.numRows//2][self.numColumns//2].write("Game Over!", False, align="center", font=("Aria1", 32, 'bold'))
                        self.gameOver = True

                    #opens up surronding values if user hits an empty cell
                    if self.valuesList[row][column] == 0:
                        self.revealImage(row-1, column-1)
                        self.revealImage(row-1, column)
                        self.revealImage(row-1, column+1)
                        self.revealImage(row, column-1)
                        self.revealImage(row, column+1)
                        self.revealImage(row+1, column-1)
                        self.revealImage(row+1, column)
                        self.revealImage(row+1, column+1)

    def leftButtonClick(self, x_cord, y_cord):
        '''
        param: x coordinate, y coordinate
        return: None
        if user presses left buton then it determines which grid cell is called.
        calls the reveal Image function and determines if user wins by clearing grid
        except bombs
        '''

        gridX = (-1 * self.numColumns) * (self.width // 2)
        gridY = (self.numRows * self.height // 2)
        
        if self.gameOver == True:
            return

        #computes the row and column from mouse click
        row = int((gridY - y_cord + (self.height // 2)) // self.height)
        column = int((x_cord - gridX + (self.width//2)) // self.width)

        #calls reveal image function
        self.revealImage(row, column)

        #checks if user clicked within bounds
        if row >= 0 and row < self.numRows:
            if column >= 0 and column < self.numColumns:
                
                #if there are no more covers then tells user they won
                game_boolean = True
                for x in range(self.numRows):
                    for y in range(self.numColumns):
                        if self.turtlesList[x][y].shape() in self.coversList and self.valuesList[x][y] != 9:
                            game_boolean = False
                            break

                #if player removes all cover images and wins then writes You Win for user
                if game_boolean:
                    self.turtlesList[self.numRows//2][self.numColumns//2].write("You Win!", False, align="center", font=("Aria1", 32, 'bold'))
                    self.gameOver = True
                
    def rightButtonClick(self, x_cord, y_cord):
        '''
        param: x coordinate and y coordinate
        return: None
        if user enters right button then function determines which grid cell is clicked
        and iterates over index of covers grid to switch between the values
        '''
        
        if self.gameOver == True:
            return
        
        #computes x and y coordinates
        grid_x = (-1 * self.numColumns) * (self.width // 2)
        grid_y = self.numRows * (self.height // 2)
        
        #computes the row and column from mouse click
        row = int((grid_y - y_cord + (self.height // 2)) // self.height)
        column = int((x_cord - grid_x + (self.width//2)) // self.width)

        #determines if the row and column clicked were within bounds
        if row >= 0 and row < self.numRows:
            if column >= 0 and column < self.numColumns:
                if not self.turtlesList[row][column].shape() in self.coversList:
                    return

                #iterates through cover list and sets turtle to cover list object
                index = self.coversList.index(self.turtlesList[row][column].shape())
                toggle_index = (index+1) % len(self.coversList)
                self.turtlesList[row][column].shape(self.coversList[toggle_index])
    
    