__author__ = "Johnathan Friend"
__purpose__= "uses python turtle to play minesweeper, uses file I/O to save and replay games\
    utilizes the Minesweeper class"

import turtle
from minesweeper import Minesweeper

def main():
    '''
    param: None
    return: None
    can open an existing mine sweeper game from a file or create a new minesweeper game
    utilizing the Minesweeper class
    '''

    #gets user input to decide for a new game or open existing saved game
    print("Enter an option from below:")
    print("1.) Continue an existing game saved in a file.")
    print("2.) Play a new game.")

    while(True):
        try:
            userGameOption = int(input("Enter 1 or 2: "))
            if userGameOption in [1, 2]:
                break
        except:
            print("\nplease enter a 1 or 2")
    
    #if user wants to open an existing save file
    if userGameOption == 1:
        valuesList = []

        #opens file that user enters
        user_file = input("Enter the existing game file name: ")
        game_file = open(str(user_file), "r")

        #reads num rows and columns, and reads grid values from file
        raw_grid_size = game_file.readline()
        clean_grid_size = raw_grid_size.split(":")
        numRows = int(clean_grid_size[0])
        numColumns = int(clean_grid_size[1])
        grid_values = game_file.readline()

        while grid_values != "":
            raw_values1 = grid_values.strip('\n')
            values = raw_values1.split(":")
            values.remove('')
            valuesList.append(values)
            grid_values = game_file.readline()
        game_file.close()

        #turns all strings from list into intengers
        for x in range(len(valuesList)):
            for y in range(len(valuesList[x])):
                valuesList[x][y] = int(valuesList[x][y])

        #makes the minesweeper game object, calls minesweeper game methods from Minesweeper class
        game = Minesweeper(800, 800, 30, 30, numRows, numColumns, [], [], valuesList, [], 0, False)
        game.startGame()
        game.createTurtles()
        game.drawGrid()
        
        #keeps window running
        turtle.mainloop()

    #if user wants to create a new game
    else:

        #gets user to decide grid size
        print("\nGrid size options:")
        print("1.) 10 x 10")
        print("2.) 10 x 15")
        print("3.) 15 x 15")
        print("4.) 20 x 20")
        while(True):
            try:
                userGrid = int(input("Enter a grid size 1, 2, 3, or 4: "))
                if userGameOption in [1, 2]:
                    break
            except:
                print("\nplease enter a 1, 2, 3, or 4")
        
        #sets grid size based on user input
        if userGrid == 1:
            numColumns = 10
            numRows = 10
        elif userGrid == 2:
            numColumns = 15
            numRows = 10
        elif userGrid == 3:
            numColumns = 15
            numRows = 15
        else:
            numColumns = 20
            numRows = 20

        #gets user to decide difficulty
        print("\nDifficulty options:")
        print("1.) beginner")
        print("2.) easy")
        print("3.) difficult")
        print("4.) expert")
        while(True):
            try:
                userDifficulty = int(input("Enter a difficulty 1, 2, 3, or 4: "))
                if userGameOption in [1, 2]:
                    break
            except:
                print("\nplease enter a 1, 2, 3, or 4")
        
        #sets difficulty based on user input
        if userDifficulty == 1:
            difficulty = 0.05
        elif userDifficulty == 2:
            difficulty = 0.10
        elif userDifficulty == 3:
            difficulty = 0.15
        else:
            difficulty = 0.20
        numBombs = difficulty * (numColumns * numRows)

        #makes the minesweeper game object, calls minesweeper game methods from Minesweeper class
        game = Minesweeper(800, 800, 30, 30, numRows, numColumns, [], [], [], [], numBombs, False)
        game.startGame()
        game.createValuesList()
        game.createTurtles()
        game.createBombs()
        game.drawGrid()
        
        #keeps window running
        turtle.mainloop()

        #ask user if they would like to save a file and opens a file and writes grid info
        user_save = int(input("Would you like to save the game (1 for YES, 2 for NO): "))
        if user_save == 1:
            save_file_name = input("Enter name to save file as: ")
            save_file = open(save_file_name, "w")
            save_file.write(str(game.numRows)+':'+str(game.numColumns)+'\n')
            for x in range(len(game.valuesList)):
                for y in range(len(game.valuesList[x])):
                    save_file.write(str(game.valuesList[x][y])+':')
                save_file.write("\n")
        else:
            print('Thanks for playing!')

if __name__ == "__main__":
    main()