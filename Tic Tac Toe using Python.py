#!/usr/bin/env python
# coding: utf-8

# In[34]:


print("Welcome to Tic Tac Toe \n")

# from IPython.display import clear_output
# clear_output()

def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board [9])
    print('-----' )
    print(board[4] + '|' + board[5] + '|' + board [6])
    print('-----' )
    print(board[1] + '|' + board[2] + '|' + board [3])
    print('-----' )
    
board =['',' ',' ',' ',' ',' ',' ',' ',' ',' ']
# display_board(board)
#start with player 1 
choose = input("Will player 1 take X or O ? \n")
i=1
position
while (i<=9):
    if(i%2 ==0):
         position = int(input("The position player 2 wants to choose : ('1-9')"))
         if board[position]==' ':
            board[position]=('O' if choose=='X' else 'X')
         else:
            print("Position already filled")
            i=i-1
    else:
         position = int(input("The position player 1 wants to choose : ('1-9')"))
         if board[position]==' ':
            board[position]=choose
         else:
            print("Position already filled")
            i=i-1
        
    display_board(board)
    if((board[1]=='X' and board[2]=='X' and board[3]=='X') or (board[1]=='O' and board[2]=='O' and board[3]=='O') ):
        if(board[1]== choose):
            print("Game over! Player 1 won the game")
        else:
            print("Game over! Player 2 won the game")
        break
    elif((board[1]=='X' and board[4]=='X' and board[7]=='X') or (board[1]=='O' and board[4]=='O' and board[7]=='O')):
        if(board[1]== choose):
            print("Game over! Player 1 won the game")
        else:
            print("Game over! Player 2 won the game")
        break
    elif((board[1]=='X' and board[5]=='X' and board[9]=='X') or (board[1]=='O' and board[5]=='O' and board[9]=='O')):
        if(board[1]== choose):
            print("Game over! Player 1 won the game")
        else:
            print("Game over! Player 2 won the game")
        break
    elif((board[2]=='X' and board[5]=='X' and board[8]=='X') or (board[2]=='O' and board[5]=='O' and board[8]=='O')):
        if(board[2]== choose):
            print("Game over! Player 1 won the game")
        else:
            print("Game over! Player 2 won the game")
        break
    
    elif((board[3]=='X' and board[6]=='X' and board[9]=='X') or (board[3]=='O' and board[6]=='O' and board[9]=='O')):
        if(board[3]== choose):
            print("Game over! Player 1 won the game")
        else:
            print("Game over! Player 2 won the game")
        break
    elif((board[3]=='X' and board[5]=='X' and board[7]=='X') or (board[3]=='O' and board[5]=='O' and board[7]=='O')):
        if(board[3]== choose):
            print("Game over! Player 1 won the game")
        else:
            print("Game over! Player 2 won the game") 
        break
    elif((board[4]=='X' and board[5]=='X' and board[6]=='X') or (board[4]=='O' and board[5]=='O' and board[6]=='O')):
        if(board[4]== choose):
            print("Game over! Player 1 won the game")
        else:
            print("Game over! Player 2 won the game")
        break
    elif((board[7]=='X' and board[8]=='X' and board[9]=='X') or (board[7]=='O' and board[8]=='O' and board[9]=='O')):
        if(board[7]== choose):
            print("Game over! Player 1 won the game")
        else:
            print("Game over! Player 2 won the game")
        break
     
    if i==9:
        print("It's a tie! Let's party")
    i= i+1
       
    
    
    

    



    



# In[ ]:





# In[ ]:





# In[ ]:




