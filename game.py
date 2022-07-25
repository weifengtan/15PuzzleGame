''' DO NOT FORGET TO ADD COMMENTS '''

from tkinter import *
import tkinter.font as font
from fifteen import Fifteen
          

def clickButton(button, gui, game):
    go = True
    new = tiles.tiles
    
    if str(button) == '.!button':
        print(button)
        if tiles.is_valid_move(1):
            tiles.update(1)
    else :
        if tiles.is_valid_move(int(str(button).strip('.!button'))):
            tiles.update(int(str(button).strip('.!button')))
    
    for i in range(len(tiles.tiles)):
        name = tiles.tiles[i]
        button = Button(gui, text = tiles.tiles[i], name=str(name),
                        bg = 'white', fg='black', font=font, height=2, width=5)
        
        button.config(command = lambda button = button, gui = gui: clickButton(button, gui, game))
        
        button.grid(row = i//4, column = i%4)
        
    if tiles.is_solved():
        gui.destroy()
    
if __name__ == '__main__':    

    # make tiles
    tiles = Fifteen()
    buttons = []

    # make a window
    gui = Tk()
    gui.title("Fifteen")
    tiles.shuffle()
    # make font
    font = font.Font(family='Helveca', size='25', weight='bold')

    # make buttons
    
    for i in range(len(tiles.tiles)):
        name = tiles.tiles[i]
        button = Button(gui, text = tiles.tiles[i], name=str(name),
                        bg = 'white', fg='black', font=font, height=2, width=5)
        
        button.config(command = lambda button = button, gui = gui, game = tiles.tiles: clickButton(button, gui, game))
        gui.nametowidget(name).configure(bg='white')
        buttons.append(button)
        button.grid(row = i//4, column = i%4) 

    
    # update the window
    gui.mainloop()
