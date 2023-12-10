
import os
import json
from enum import Enum

class Actions(Enum):
    PRINT = 1
    ADD = 2
    SEARCH = 3
    DELETE =4
    EXIT = 5

contacts =[]
my_data_file='contacts.json'

def menu():
    for x in Actions:
        print(f'{x.value} - {x.name}')
   
    return Actions(int(input("Enter your selection:")))

def load_data():# load a list from a file
    global contacts
    try:
        with open(my_data_file, 'r') as file:
            json_string = file.read()
            contacts = json.loads(json_string)
    except: pass

def main():
    os.system('cls' if os.name == 'nt' else 'clear')# clear screen
    load_data() #load data from a file

    while(True):
        userSelection=menu() #display a menu and get user selection and  implements menu
        if userSelection == Actions.EXIT: exit_func()
        if userSelection ==  Actions.PRINT: print(contacts)
        if userSelection ==  Actions.SEARCH: pass
        if userSelection ==  Actions.ADD: add_contact()

def add_contact():
    contacts.append({"Name":input("Enter your name:"),"Last":input("Enter your Lastname:")})

def exit_func():
    json_string = json.dumps(contacts)
    # save the list in a file
    with open(my_data_file, 'w') as file:
        file.write(json_string)
    print("c ya") 
    exit()

if __name__ == "__main__":
    main()