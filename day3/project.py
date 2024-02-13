journey_result = "Game Over"
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")
left_of_right = input("Left or Rigth: ").lower()
if(left_of_right == 'left'):
    swing_or_wait = input("Swing or Wait: ").lower()
    if(swing_or_wait == 'wait'):
        door = input("Which door? Red, Blue or Yellow? ").lower()
        if(door == "yellow"):
            journey_result = "You Win!"
print(journey_result)