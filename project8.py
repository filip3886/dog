dictionary = {}

def print_element():
    if dictionary:
        for key, val in dictionary.items():
            print(key, val)
    else:
        print("is empty")

def delete_element():
    print_element()
    choise=(input("enter the key which u need to delete: "))
    if choise in dictionary.keys():
        dictionary.pop(choise)
        print_element()
    else:
        print("wrong key :")

def write_element():   
    choise = int(input("How much people u want to add: "))
    for i in range(choise):
        name_key = input("Enter the name: ")
        date_value = input("Enter the date: ")
        dictionary.update({name_key:date_value}) 
    print("Sucesful write!")

def start():
    while True:
        choise = int(input("Enter choise(1 - print, 2 - delete, 3 - write, 4 - exit): "))
        if choise == 1:
            print_element()
        if choise == 2:
            delete_element()
        if choise == 3:
            write_element()
        if choise == 4:
            break
        if choise !=(1,2,3,4):
            print("")


start()