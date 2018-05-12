import display


# 'l' - Go left
# 'r' - Go right
# 'u' - Go up
# 'd' - Go down
# 'y/n' - Replies 'Yes' or 'No' when prompted
# 'i' - quickly shows you your items
# 'p' - shows you what's in the room'
# 'c' - Brings up the control screen again

def menu(room):
    directions = ['r', 'l', 'u', 'd']
    userin = ''
    while(1):
        userin = input("Type a command or type . if you want to specify an item")
        if userin == '.':
            item()
        elif userin == 'r':
            if room.right != null:
                break
            else:
                print("You can't go that way.\n")
        elif userin == 'l':
            if room.left != null:
                break
            else:
                print("You can't go that way.\n")
        elif userin == 'u':
            if room.up != null:
                break
            else:
                print("You can't go that way.\n")
        elif userin == 'd':
            if room.down != null:
                break
            else:
                print("You can't go that way.\n")
               
        elif userin == 'i':
            display.userItems(user)
            return 
