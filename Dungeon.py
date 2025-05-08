def adventure_game():
    print("welcome to Dungeon! your objective is found the treasure.")
    print("chose the actions carefully to avoid the traps and mistakes." )

    try:
        print("you are in front to 3 doors: [1, 2 and 3]")
        door = int(input("which door do you choose?:"))

        if door == 1:
            print("You found a monster, it attacked you, but you escape.")
        elif door == 2:
            print("congratulations, you found a treasure.")
            try:
                    print("the treasure is locked, you can do 3 things: [1 - broke this whith your hands, 2 - use witchcraft or 3 - take it home]")
                    choice =  int(input("which choice do you choose?:"))

                    if choice == 1:
                        print("you broke your hands.")
                    elif choice == 2:
                        print("you explode your house.")
                    elif choice == 3:
                        print("the treasure fell at your feet and you died in the middle of the way.")
            except ValueError:
                    print("this choice doesn't exists.")
            finally:
                    print("")
            

            return
        elif door == 3:
            print("unfortunately a monster attacked you and you died." )
    except ValueError:
        print("this door doesn't exists.")
    finally:
        print("The end")

adventure_game()