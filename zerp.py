import display

items = []



def openlope():
    display.openlope()
    items.append("Cuffkey")
    return


def freedcuff():
    print("Well done!")
    quit()










#      Beginning of the game
#
#
#
#
#    
items = []
display.title()
input("Press enter to start! ")

display.menu()
input("Press enter to continue!")

while(1):
    display.room_1()
    userin = ''
    userin = input("\nType a command or the name of the object you want to interact with.\n")
    if userin.lower() == 'handcuff':
        if "Cuffkey" in items:
            freedcuff()
        else:
            print("\nYou can't interact with the handcuff at the moment.\n")
    elif userin.lower() == 'envelope':
        if "Cuffkey" in items:
            print("You have already opened the envelope.")
        else:
            openlope()
    elif userin == 'r':
        print("\nYou can't go that way.\n")
    elif userin == 'l':
        print("\nYou can't go that way.\n")
    elif userin == 'u':
        print("\nYou can't go that way.\n")
    elif userin == 'd':
        print("\nYou can't go that way.\n")
    elif userin == 'i':
        if items is None:
            print("\nYou don't have anything at the moment")
        else:
            print(items)
    else:
        print("\nPlease enter either a valid command or an item.\n")



 
