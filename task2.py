def turn_right():
    turn_left()
    turn_left()
    turn_left()
   
def game():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
i = 0    
while i < 6:
    game()
    i += 1
    
print("you won")    
    
    

