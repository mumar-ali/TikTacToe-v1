
board = [["EMPTY" for i in range(3)] for j in range(3)]
board[0][0] =1
board[0][1] =2
board[0][2] =3
board[1][0] =4
board[1][1] ="X"
board[1][2] =6
board[2][0] =7
board[2][1] =8
board[2][2] =9

def display_board(board):

    counter = -1
    for i in range (26):
        counter += 1
        if counter ==  0 :
            print("+------------------------------+")
        elif counter == 8:
            print("+------------------------------+")
        elif counter == 16:
            print("+------------------------------+")
        elif counter == 25:
            print("+------------------------------+")
        elif counter == 4:
            print("|   ", board[0][0] ,"   |   ", board[0][1] ,"    |   ", board[0][2] ,"   |")
        elif counter == 12:
            print("|   ", board[1][0] ,"   |   ", board[1][1] ,"    |   ", board[1][2] ,"   |")
        elif counter == 20:
            print("|   ", board[2][0] ,"   |   ", board[2][1] ,"    |   ", board[2][2] ,"   |")
        else:
            print("|         |          |         |")


def enter_move(board):
    user_move  = int(input("ENTER NUMBER: "))
    if user_move == 1:
        if board[0][0] != "O" and board[0][0] != "X":
            board[0][0] = "O"
            return ("fine")
        else:
            return ("square taken")
    elif user_move == 2:
        if board[0][1] != "O" and board[0][1] != "X":
            board[0][1] = "O"
            return ("fine")
        else: 
            return ("square taken")
    elif user_move == 3:
        if board[0][2] != "O" and board[0][2] != "X":
            board[0][2] = "O"
            return ("fine")
        else:
            return ("square taken")
    elif user_move == 4:
        if board[1][0] != "O" and board[1][0] != "X":
            board[1][0] = "O"
            return ("fine")
        else:
            return ("square taken")
    elif user_move == 5:
            return ("square taken")
    elif user_move == 6:
        if board[1][2] != "O" and  board[1][2] != "X":
            board[1][2] = "O"
            return ("fine")
        else:
            return ("square taken")
    elif user_move == 7:
        if board[2][0] != "O" and board[2][0] != "X":
            board[2][0] = "O"
            return ("fine")
        else:
            return ("square taken")
    if user_move == 8:
        if board[2][1] != "O" and board[2][1] != "X":
            board[2][1] = "O"
            return ("fine")
        else:
            return ("square taken")
    if user_move == 9:
        if board[2][2] != "O" and board[2][2] != "X":
            board[2][2] = "O"
            return ("fine")
        else:
            return ("square taken")
             


def victory_for(board, sign):
    
    if board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        if sign == "X":
            return 1
        else:
            return 2
    elif board[0][0]  == sign and board[0][1] == sign and board[0][2] == sign:
        if sign == "X":
            return 1
        else:
            return 2

    elif board[0][0]  == sign and board[1][1] == sign and board[2][2] == sign:
            if sign == "X":
                return 1
            else:
                return 2
                
    elif board[0][1]  == sign and board[1][1] == sign and board[2][1] == sign:
                if sign == "X":
                    return 1
                else:
                    return 2
    elif board[0][2]  == sign and board[1][2] == sign and board[2][2] == sign:
                if sign == "X":
                    return 1
                else:
                    return 2

    elif board[0][2]  == sign and board[1][1] == sign and board[2][0] == sign:
                if sign == "X":
                    return 1
                else:
                    return 2
    
    elif board[1][0]  == sign and board[1][1] == sign and board[1][2] == sign:
                if sign == "X":
                    return 1
                else:
                    return 2
    elif board[2][0]  == sign and board[2][1] == sign and board[2][2] == sign:
                if sign == "X":
                    return 1
                else:
                    return 2
    elif board[0][0] != 1:
        if board[0][1]  != 2:
            if board[0][2] != 3:
                if board[1][0 ]  != 4:
                    if board[1][1] != 5:
                        if board[1][2]  != 6:
                            if board[2][0] != 7:
                                if board[2][1] != 8:
                                    if board[2][2] != 9:
                                        return 3 
                                    else:
                                        return 4  
                                else:
                                    return 4  
                            else:
                                return 4 
                        else:
                            return 4
                    else:
                        return 4
                else:
                    return 4
            else:
                return 4
        else:
            return 4
    else:
        return 4                                     

        

def make_list_of_free_fields(board ):
        valid_move = []
        for i in range (len(board)):
            for j in range (len(board)):
                tup = ( i, j )
                if tup == (0, 0):
                    if board[0][0] != "O" and board[0][0] != "X":
                        valid_move.append(tup) 
                if tup == (0, 1):
                    if board[0][1] != "O" and board[0][1] != "X":
                        valid_move.append(tup)         
                if tup == (0, 2):
                    if board[0][2] != "O"  and board[0][2] != "X":
                        valid_move.append(tup)         
                if tup == (1, 0):
                    if board[1][0] != "O" and board[1][0] != "X":
                        valid_move.append(tup)         
                if tup == (1, 2):
                    if board[1][2] != "O" and board[1][2] != "X":
                        valid_move.append(tup)
                if tup == (2, 0):
                    if board[2][0] != "O" and board[0][0] != "X":
                        valid_move.append(tup)
                if tup == (2, 1):
                   if board[2][1] != "O" and board[2][1] != "X":
                        valid_move.append(tup)
                if tup == (2, 2):
                    if board[2][2] != "O" and board[2][2] != "X":
                        valid_move.append(tup)
        return valid_move

                       
                      
     
          
             
  
             


    

    

        
def draw_move(board):
    leng = len(make_list_of_free_fields(board ))
    from random import randrange
    gg = (randrange(leng))
    move = make_list_of_free_fields(board )
    valid_move = move[gg]
    print (move)
    print (leng)
    print (valid_move)
    if valid_move == (0, 0):
        board[0][0] = "X"
        print (valid_move)
    else:
        print("1")
    if valid_move == (0, 1):
        board[0][1] = "X"
        print (valid_move)
    else:
        print("2")
    if valid_move == (0, 2):
        board[0][2] = "X"
        print (valid_move)
    else:
        print("3")
    if valid_move == (1, 0):
        board[1][0] = "X"
        print (valid_move)
    else:
        print("4")
    if valid_move == (1, 2):
        board[1][2] = "X"
        print (valid_move)
    else:
        print("6")
    if valid_move == (2, 0):
        board[2][0] = "X"
        print (valid_move)
    else:
        print("7")
    if valid_move == (2, 1):
        board[2][1] = "X"
        print (valid_move)
    else:
        print("8")
    if valid_move == (2, 2):
        board[2][2] = "X"
        print (valid_move)
    else:
        print("9")

        
    











ans = False


display_board(board)
w = enter_move(board)
while w == "square taken":
    print("square taken")
    w = enter_move(board)

while  ans == False:


    if  w == "fine":


        display_board(board)
        result = victory_for(board, "O")
        print (result)
        if result == 2:
            print ("YOU WIN")
            ans = True
        elif result == 3:
            print ("DRAW")
            ans = True
        elif result == 4:
            draw_move(board)
            display_board(board)
            result = victory_for(board, "X")
            print(result)
            if result == 1:
                print ("I WIN")
                ans = True
            elif result == 3:
                print ("DRAW")
                ans = True
            else:
                w = enter_move(board)
                
        else:
            print("?")

    else:
        print ("square taken")
        w = enter_move(board)
        
    

    