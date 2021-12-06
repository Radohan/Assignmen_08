#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# RadoslawHankiewicz, 2021-Dec-5, updated file
#------------------------------------------#

# -- DATA -- #

strFileName = 'cdInventory.txt'
lstOfCDObjects = []


class CD:
    
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    # DONE Add Code to the CD class
    
    def __init__(self, cd_id, cd_title, cd_artist):
        self.cd_id = cd_id
        self.cd_title = cd_title
        self.cd_artist = cd_artist
    
# -- PROCESSING -- #

class FileIO:
    
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # DONE Add code to process data to a file
      
    def save_inventory(lst, file_name):
        objFile = open(file_name, 'a')
        for obj in lst:
            objFile.write('{}, {}, {}\n'.format(obj.cd_id, obj.cd_title, obj.cd_artist))
        objFile.close()
    
    # DONE Add code to process data from a file

    def load_inventory(file_name, lst):
        lst.clear()  
        objFile = open(file_name, 'r')
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)')
        for line in objFile:
                data = line.strip().split(',')
                lst.append(CD(data[0], data[1],data[2]))
                print("{}, {}, {}".format(data[0], data[1], data[2]))
        return lst
        objFile.close()
             
# -- PRESENTATION (Input/Output) -- #

class IO:
    
    # DONE add docstring
    
    """Handling Input / Output

    properties:

    methods:
        read_file(file_name, lst) --> None
        print_menu() --> None
        menu_choice() --> choice
        show_inventory(lst) --> None
        userInput() --> cd_id, cd_title, cd_artist

    """
    # DONE add code to show menu to user
    
    def read_file(file_name, lst):
        lst.clear() 
        objFile = open(file_name, 'r')
        for line in objFile:
                data = line.strip().split(',')
                lst.append(CD(data[0], data[1],data[2]))
        return lst
        objFile.close()
    
    @staticmethod
    def print_menu():
        print('Menu\n\n[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] Exit\n')
    
    # DONE add code to captures user's choice
    
    def menu_choice():
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
            print()  # Add extra space for layout
            return choice
    
    # DONE add code to display the current data on screen
    
    def show_inventory(lst):
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)')
        for obj in lst:
            print("{}, {}, {}".format(obj.cd_id, obj.cd_title, obj.cd_artist))

    # DONE add code to get CD data from user
    
    def userInput():
        cd_id = int(input('Enter ID: ').strip())
        cd_title = input('What is the CD\'s title? ').strip()
        cd_artist = input('What is the Artist\'s name? ').strip()
        return cd_id, cd_title, cd_artist

# -- Main Body of Script -- #
# DONE Add Code to the main body
# Load data from file into a list of CD objects on script start

lstOfCDObjects = IO.read_file('cdInventory.txt', lstOfCDObjects)

# Display menu to user

while True:
    
    IO.print_menu()
    strChoice = IO.menu_choice()
    
    # let user exit program

    if strChoice == 'x':
        break
    
    # show user current inventory
    
    if strChoice == 'i':
         IO.show_inventory(lstOfCDObjects)
         continue
 
    # let user add data to the inventory
    
    elif strChoice == 'a':
        cd_id, cd_title, cd_artist = IO.userInput()
        newCD = CD(cd_id, cd_title, cd_artist)
        lstOfCDObjects.append(newCD)
        IO.show_inventory(lstOfCDObjects)
        continue

    # let user save inventory to file
    
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            # DONE move processing code into function
            FileIO.save_inventory(lstOfCDObjects, "cdInventory.txt")
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    
    # let user load inventory from file
    
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = FileIO.load_inventory('cdInventory.txt', lstOfCDObjects)
            #print(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue