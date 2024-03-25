#Question 2 
shopping_list= []

def add_list():
    global shopping_list
    while True:
        action = input("Would you like to [A]dd or [R]emove from the shopping list? If all done press [Q]uit ").upper()#Task 1
        if action == 'A':
            while True:
                add = input("What would you like in the shopping list? If you are done adding press [Q]uit ").upper()
                if add == 'Q':
                    break
                shopping_list.append(add)
        elif action == 'R':#Task 2
            re = input("What would you like to remove from the shopping list? If you are done removing press [Q]uit ").upper()
            if re == 'Q':
                break
            shopping_list.remove(re)
        elif action == 'Q':
            break
        else:
            print("Invalid selection")

#Task 3
def list_displayed():
    global shopping_list
    counter = 0
    print("\tShopping list")
    for i in shopping_list:
        counter += 1
        print ( f"\tItem number {counter}:\n\t{i}")

add_list()
list_displayed()