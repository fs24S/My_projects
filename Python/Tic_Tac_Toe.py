''' 
Game: Tic Tac Toe
Player one chooses the row and column's position, then player two selects the row and column.
The game will end when one player puts three same numbers in a row, column, or diagonal.
'''

import itertools

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This positon is occupado ! Choose another! ")
            return game_map, False
        print("   "+"  ".join([str(i) for  i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player
        for a, i in enumerate(game_map):
            print(a, i)
        return game_map, True
    except IndexError as e: 
        print("Error",e)
        return game_map, False
    except Exception as e:
        print("Something went very wrong!",e)
        return game_map, False

def win(current_game):
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    for row in game:
        if all_same(row):
            print(f"Player {row[0]} is the Winner!")
            return True

    for col in range(len(game)):
        check = []
        for column in game:
            check.append(column[col])

        if all_same(check):
            print(f"Player {check[0]} is the Winner!")
            return True
     
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f"Player {diags[0]} is the Winner!")
        return True
  
    diags = []
    for row, col in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} is the Winner!")
        return True

    return False


play = True
while play:
    game = [[0,0,0],
            [0,0,0],
            [0,0,0]]
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")
        played = False

        while not played:
            Player_row = int(input("Choose positon of row: "))
            Player_colum = int(input("Choose positon of colum: "))
            game, played = game_board(game, current_player, Player_row,  Player_colum)
        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n) ")
            if again.lower() == "y":
                print("Restarting")
            elif again.lower() == "n":
                print("Bye")
                play = False
            else:
                print("Not a valid answer, try again ")
                play = False



