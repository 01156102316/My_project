
""""
Number scrabble is played with the list of numbers between 1 and 9. Each player takes
turns picking a number from the list. Once a number has been picked, it cannot be picked
again. If a player has picked three numbers that add up to 15, that player wins the game.
However, if all the numbers are used and no player gets exactly 15, the game is a draw
"""
# set numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player1_numbers = []
player2_numbers = []
# welcome message and display statues
print("Welcome to the Number scrabble ")#welcome message
# the game rules
print("'This game  is played with the list of numbers between 1 and 9 \nEach player takes turns picking a number from the list")
print("Once number has been picked ,it cannot  be picked again\nif a player has picked three numbers that add up to 15,that player wins the game ")
print("if all the numbers are used and no player gets exactly 15 the game is draw ")
input("press  any key to start the game ")

def check_thr_winner(player_numbers):
    for i in range(len(player_numbers)):
        for x in range(i+1,len(player_numbers)):
           for a in range(x+1 , len(player_numbers)):
                if player_numbers[i]+player_numbers[x]+player_numbers[a]==15 :
                    return True
    return False
def scrabble_game():#lets user choose number between 1 and 9

     for i in range(1, 10):
         while numbers:
             while True:
                 print(numbers)
                 try:
                     choice_num1 = int(input("player 1 please entre number between 1 and 9 : "))
                     if int(choice_num1) in numbers:
                         numbers.remove(choice_num1)
                         player1_numbers.append(choice_num1)
                         break
                     else:
                         print("this number not in range or chosen before please try again")  # check the number in range or chosen before
                 except ValueError:
                     print("please entre a valid number ")
                     continue

             if check_thr_winner(player1_numbers):
                 print("player 1 is wins ")
                 return

             break



         while numbers:
             while True:
                 print(numbers)
                 try:
                  choice_num2 = int(input("player 2 please entre number between 1 and 9 :" ))
                  if int(choice_num2) in numbers:
                     numbers.remove(choice_num2)
                     player2_numbers.append(choice_num2)
                     break
                  else:
                     print("this number not in range or chosen before please try again")
                 except ValueError:
                     print("please entre a valid number")
                     continue
             if check_thr_winner(player2_numbers):
                 print("player 2 is wins ")
                 return


             break




     print("this game is draw")
scrabble_game()
input()
