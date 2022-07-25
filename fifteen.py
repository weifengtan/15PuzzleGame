''' DO NOT FORGET TO ADD COMMENTS '''

import numpy as np
from random import choice

class Fifteen:
    
    def __init__(self, size = 4):
        
        self.tiles = [i for i in range(1,size**2)] + [' ']
        self.adj = [[1,4], [0,2,5], [1,3,6], [2,7], [0,5,8], [1,4,6,9], [2,5,7,10],
                    [3,6,11], [4,9,12], [5,8,10,13], [6,9,11,14], [7,10,15],
                    [8,13], [9,12,14], [10,13,15], [11,14]]

    def update(self, move):
        if self.is_valid_move(move) == True:
            if move == 0:
                num = 1
                space = self.tiles.index(' ')
            else:
                num = self.tiles.index(move)
                space = self.tiles.index(' ')

            self.transpose(num,space)
        
    def transpose(self, i, j):
        self.tiles[i], self.tiles[j] = self.tiles[j], self.tiles[i]
        

    def shuffle(self, steps=100):
        number_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        while steps != 0:
            random_num = choice(number_list)
            if self.is_valid_move(random_num) :
                num = self.tiles.index(random_num)
                space = self.tiles.index(' ')
                self.transpose(random_num, space)
                steps -= 1
                      
        
    def is_valid_move(self, move):
        i = self.tiles.index(move)
        j = self.tiles.index(' ')
        return i in self.adj[j]

    def is_solved(self):
        solved_board = [i for i in range(1,4**2)] + [' ']
        if solved_board == self.tiles:
            return True
        else:
            return False 

    def draw(self):
        new = np.reshape(self.tiles, (4,4))
        new_string = ''
        numbers = '123456789'
        row = 0
        
        new_string += '+---+---+---+---+\n'
        for one, i in enumerate(new):
            for two, j in enumerate(i):
                string = new[one][two]
                if one > row:
                    new_string += '\n'
                    new_string += '+---+---+---+---+'
                    new_string += '\n'
                    row = one 

                if two == 0:
                    new_string += '|'
                    
                if string.isnumeric() :
                     
                    if len(str(string)) == 1 :
                        new_string += ' '
                        new_string += string
                        new_string += ' '
                        new_string += '|'
                        
                    else:
                        new_string += string
                        new_string += ' '
                        new_string += '|'
                elif string == ' ' :
                    new_string += ' '
                    new_string += string
                    new_string += ' '
                    new_string += '|'

                
        new_string += '\n'
        new_string += '+---+---+---+---+'
        print (new_string)
        return new_string
        
    def __str__(self):
        new = np.reshape(self.tiles, (4,4))
        new_string = ''
        numbers = '123456789'
        row = 0 
        for one, i in enumerate(new):
            for two, j in enumerate(i):
                string = new[one][two]
                if one > row:
                    new_string += '\n'
                    row = one 
                    
                if string.isnumeric() :
                     
                    if len(str(string)) == 1 :
                        new_string += ' '
                        new_string += string
                        new_string += ' '
                        
                    else:
                        new_string += string
                        new_string += ' '
                elif string == ' ' :
                    new_string += ' '
                    new_string += string
                    new_string += ' '
                
        new_string += '\n'
        return new_string
    

if __name__ == '__main__':
    
    game = Fifteen()
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False
    
    '''You should be able to play the game if you uncomment the code below'''
    
    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')
    
    
    
        
