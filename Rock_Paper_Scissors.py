import random as rd


#Controls the main game While-loop
KEY = True
#For visual/display interaction only
SEPARATION = "*" * 72
#Variable assignment using tuple unpacking 
x, y, z = "ROCK", "PAPER", "SCISSORS",
#Game Go-to Options 
a, b, c = "CHANGE", "HELP", "BEGIN"


#Returns Information about the Gane 
def GameInfo():
    return ("""
User gets to pick either Rock, Paper or Scissors.
Depending on what the choice of the User is(in comparison to the Computer pick), we can determine if there is a winner or if it is a draw.
#Choice: Rock wins Scissors
#Choice: Paper wins Rock
#Choice: Scissors wins Paper
If the Choices of User and Computer is the same, then it is a DRAW
""")
    
    
#Returns Completed Strings
def AutoFill(n):
    if n.startswith("R"):
        return "ROCK"
    elif n.startswith("P"):
        return "PAPER"
    elif n.startswith("S"):
        return "SCISSORS"
    else: 
        return "Invalid Input"

                
#Decorates any string passed as an argument 
def Style(n):
    print(SEPARATION )
    print( f"●●● {n} ●●●".center(63, " "))
    print(SEPARATION )    
Style("START GAME")


#Outputs Game instructions for the user 
print(f"You can represent {x} by r, {y} by p and {z} by s . \nType {b} to read Game Info, {a} to change Player Name or {c} to Start Game")


user_name = "Python"
user_scores = 0
comp_scores = 0

while KEY:
    try:
        begin = input("(CHANGE/HELP/BEGIN)").upper()
        assert begin == "CHANGE" or begin == "HELP" or begin == "BEGIN"
        if begin == "HELP":
            print(GameInfo())
            print("\nStarting Game now")
            break
        elif begin == "CHANGE":
            user_name = input("Your name: ")
            continue 
        elif begin == "BEGIN":
            break
    except: 
        continue 
    
        

while KEY:     # Main Game Loop 
   
    #Combinations of winning/draw patterns 
    COMBO = ([x,y],[z,x],[y,z],[x,z],[y,x],[z,y],[x,x],[y,y],[z,z])
    
    #Choices to make in the game
    game_choices = x, y, z 
    
    #For catching User-input Error
    try:
        #Prompts user for an input
        user_pick = input(f">{x}/{y}/{z}: ").upper()
        #Gets input equivalent AutoFill strings 
        Auto_Comp = AutoFill(user_pick)
        #If input equivalent AutoFill strings not valid
        if Auto_Comp == "Invalid Input":
            #Raise error
            raise NameError
   #If Error         
    except NameError:
        print(Auto_Comp)
        continue
    
    #Randomly selected Computer choice 
    comp_pick = game_choices[rd.randint(0,2)]
    
    #Combination of User choice, Computer choice 
    use = [Auto_Comp, comp_pick]
    
    #if Computer choice wins User choice 
    if (use == COMBO[0]) or ( use == COMBO[1]) or ( use== COMBO[2]):
        print("comp_pick: ", comp_pick)
        print("Computer WINS")
        comp_scores += 1
        print(f"{user_name} {user_scores} : {comp_scores} Computer ")
        
    #If User choice wins Computer choice  
    elif ( use == COMBO[3]) or (use == COMBO[4])or  ( use== COMBO[5]):
        print("comp_pick: ", comp_pick)
        print(f"{user_name} WINS")
        user_scores += 1
        print(f"{user_name} {user_scores} : {comp_scores} Computer ")
        
    #If User Choice equals Computer Choice 
    elif ( use == COMBO[6]) or ( use == COMBO[7]) or ( use == COMBO[8]):
        print("comp_pick: ", comp_pick)
        print("DRAW")
        print(f"{user_name} {user_scores} : {comp_scores} Computer" )
    
    #Prompts User to Continue game or End game
    option = " "
    while len(option) != 0:
        option = input("Do you want to continue(Yes/No): ").lower()
        #If yes
        if option.startswith('y'):
            #Continue the game
            break
        #If no
        else:
            #End the game
            Style("END GAME")
            print(f"{user_name} {user_scores} : {comp_scores} Computer ")
            KEY = False
            break
            
            

    
            

