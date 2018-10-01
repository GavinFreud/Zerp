import display

items = []
start = 1
'''
def floor2_1():
    while(1):
        display.floor1_1()
        userin = ''
        userin = input("\nType a command or the name of the object you want to interact with.\n")
        if userin.lower() == '':
        elif userin.lower() == '':
        elif userin.lower() == 'e':
             floor2_1()
        elif userin.lower() == 'w':
             floor1_2()
        elif userin.lower() == 'n':
  
        elif userin.lower() == 's':
             room_start()
        elif userin.lower() == 'i':
            if len(items) == 0:
                print("\nYou don't have anything at the moment.")
            else:
                print(items)
        elif userin.lower() == 'c':
            display.controls()
        else:
            print("\nPlease enter either a valid command or an item.\n")

'''

'''
def floor1_2():
    while(1):
        display.floor1_1()
        userin = ''
        userin = input("\nType a command or the name of the object you want to interact with.\n")
        if userin.lower() == '':
        elif userin.lower() == '':
        elif userin.lower() == 'e':
             floor2_1()
        elif userin.lower() == 'w':
             floor1_2()
        elif userin.lower() == 'n':
             
        elif userin.lower() == 's':
             room_start()
        elif userin.lower() == 'i':
            if len(items) == 0:
                print("\nYou don't have anything at the moment.")
            else:
                print(items)
        elif userin.lower() == 'c':
            display.controls()
        else:
            print("\nPlease enter either a valid command or an item.\n")

def end():

def notyet():
'''
'''
def floor1_1():
    while(1):	
        display.floor1_1()
        userin = ''
        userin = input("\nType a command or the name of the object you want to interact with.\n")
        if userin.lower() == 'television':
        elif userin.lower() == 'bookshelf':
        elif userin.lower() == 'e':
             floor2_1()
        elif userin.lower() == 'w':
             floor1_2()
        elif userin.lower() == 'n':
             if "mainkey" in items:
                 end()
             else:
                 notyet()
        elif userin.lower() == 's':
             room_start()
        elif userin.lower() == 'i':
            if len(items) == 0:
                print("\nYou don't have anything at the moment.")
            else:
                print(items)
        elif userin.lower() == 'c':
            display.controls()
        else:
            print("\nPlease enter either a valid command or an item.\n")

'''
def room_start():
    while(1):
        if start == 1:
            start = 0
            display.start()
        else:
            display.back_start()
        userin = ''
        userin = input("\nType a command or the name of the object you want to interact with.\n")
        if userin.lower() == 'computer':
            if password in items:
               print('good stuff')
            else:
               display.computer_1();
        elif userin.lower() == 'desk':
               display.desk_stuff()
        elif userin == 'e':
            print("\nYou can't go that way.\n")
        elif userin == 'w':
            print("\nYou can't go that way.\n")
        elif userin == 'n':
            print("\nYou can't go that way.\n")
        elif userin == 's':
            print("\nYou can't go that way.\n")
        elif userin == 'i':
            if len(items) == 0:
                print("\nYou don't have anything at the moment")
            else:
                print(items)
        elif userin == 'c':
            display.controls()
        else:
            print("\nPlease enter either a valid command or an item.\n")

def freedcuff():
    while(1):
        display.freedcuff()
        userin = ''
        userin = input("\nType a command or the name of the object you want to interact with.\n")
        if userin == 'e':
            print("\nYou can't go that way.\n")
        elif userin == 'w':
            print("\nYou can't go that way.\n")
        elif userin == 'n':
            room_start()
        elif userin == 's':
            print("\nYou can't go that way.\n")
        elif userin == 'i':
            if len(items) == 0:
                print("\nYou don't have anything at the moment")
            else:
                print(items)
        elif userin == 'c':
            display.controls()
        else:
            print("\nPlease enter either a valid command or an item.\n")


def openlope():
    display.openlope()
    items.append("Cuffkey")
    return

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
    elif userin == 'e':
        print("\nYou can't go that way.\n")
    elif userin == 'w':
        print("\nYou can't go that way.\n")
    elif userin == 'n':
        print("\nYou can't go that way.\n")
    elif userin == 's':
        print("\nYou can't go that way.\n")
    elif userin == 'i':
        if items is None:
            print("\nYou don't have anything at the moment")
        else:
            print(items)
    elif userin == 'c':
        display.controls()
    else:
        print("\nPlease enter either a valid command or an item.\n")



 
