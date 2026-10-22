#NBAProspects.py

"""This program will evaluate NBA prospects based on statistics the user
gives. It will evalute guards, centers, and fowards, and tell the user there
scouting report."""

print("Welcome to the NBA Draft Prospect Evaluator!")

player = input("Enter the player's position (Guard, Forword, or Center):")

player = player.upper()

if player == "GUARD":
    PPG = float(input("Enter points per game:"))
    APG = float(input("Enter assists per game:"))
    TPP = float(input("Enter three-point percentage:"))
    
    if PPG >= 18:
        if APG >= 6:
            if TPP >= 38:
                print("SCOUTING RESULT: LOTTERY PICK")
                
    if PPG >= 18:
        if APG >= 6:
            if TPP < 38:
                print("SCOUTING RESULT: FIRST-ROUND PROSPECT")

    if PPG >= 18:
        if APG < 6:
            print("SCOUTING RESULT: SCORING SPECIALIST")
            
    if PPG < 18:
        if APG >= 7:
            print("SCOUTING RESULT: PASS-FIRST PROSPECT")
            
    if PPG < 18:
        if APG < 7:
            print("SCOUTING RESULT: NEEDS MORE DEVELOPMENT")
            
if player == "FORWARD":
    PPG = float(input("Enter points per game:"))
    RPG = float(input("Enter rebounds per game:"))
    FGP = float(input("Enter feild-goal percentage:"))
    
    if PPG >= 15:
        if RPG >= 7:
            if FGP >= 50:
                print("SCOUTING RESULT: LOTTERY PICK")
                
    if PPG >= 15:
        if RPG >= 7:
            if FGP < 50:
                print("SCOUTING RESULT: FIRST-ROUND PROSPECT")
                
    if PPG >= 15:
        if RPG < 7:
            print("SCOUTING RESULT: OFFENSIVE SPECIALIST")
            
    if PPG < 15:
        if RPG >= 9:
            print("SCOUTING RESULT: DEFENSIVE/REBOUNDING PROSPECT")
            
    if PPG < 15:
        if RPG < 9:
            print("SCOUTING RESULT: NEEDS MORE DEVELOPMENT")
            
if player == "CENTER":
    RPG = float(input("Enter rebounds per game:"))
    BPG = float(input("Enter blocks per game:"))
    FGP = float(input("Enter field-goal percentage:"))
    
    if RPG >= 10:
        if BPG >= 2:
            if FGP >= 55:
                print("SCOUTING RESULT: LOTTERY PICK")
                
    if RPG >= 10:
        if BPG >= 2:
            if FGP < 55:
                print("SCOUTING RESULT: FIRST-ROUND PROSPECT")
                
    if RPG >= 10:
        if BPG < 2:
            print("SCOUTING RESULT: STRONG REBOUNDING PROSPECT")
            
    if RPG < 10:
        if BPG >= 2.5:
            print("SCOUTING RESULT: DEFENSIVE SPECIALIST")
            
    if RPG < 10:
        if BPG < 2.5:
            print("SCOUTING RESULT: NEEDS MORE DEVELOPMENT")