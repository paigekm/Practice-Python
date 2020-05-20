import random

def get_integer(m):
    my_integer = int(input(m))
    return my_integer

def get_string(m):
    my_string = input(m)
    return my_string
    print("."*100)



def print_at_index(L):
    my_index = get_integer("Please enter index number: -> ")
    output = "The value -- {} -- is at index {} in the list".format(L[my_index], my_index)
    print(output)
    print("."*100)
    
# basic print list
def print_list(L):
    for x in L:
        print(x)
    print("."*100)

# print with index as 1
def print_list_indexes(L):
    for i in range(0, len(L)):
        # i is the counter, L is value in the list
        print( "{} : {}".format(i, L[i]))
    print("."*100)
        
def add_item(L):
    my_item = get_string("Please enter a new item: -> ")
    L.append(my_item)


def find_item(L):
    item = get_string("Who do you want to find: -> ")
    if item in L:
        index_num = L.index(item)
        output = "{} has been found and is at index number {}".format(L[index_num], index_num)
        print(output)
    else:
        print("{} is not in the list".format(item))
    print("." * 100)


# could integrate with find_item function
def remove_item(L):
    item = get_string("Who do you want to remove? -> ")
    # need to check it's there first
    if item in L:
        # standard python method to remove it
        L.remove(item)
        output = "{} has been removed from the list".format(item)
        print(output)
    else:
        print("{} could not be found".format(item))


def sort_list(L):
    L.sort()



def shuffle_list(L):
    random.shuffle(L)




def change_value(L):
    # print menu sp user has index numbers
    print_list_indexes(L)
    index_num = get_integer("Please choose the index number: -> ")
    new_value = get_string("Please enter new value: -> ")
    # we tested and now know we have all the values we need
    #print(index_num)
    #print(new_value)
    # accessing or doing anything with a list you will use []
    # temporarily hold old value for print out
    old_value = L[index_num]
    # update value
    L[index_num]= new_value
    # confirmation message that this change has occurred
    output="The old value of {} is now changed to {}".format(old_value, L[index_num])
    print(output)



#function tests
#print_list_indexes(my_list)
#print_list(my_list)
#add_item(my_list)
#print_list(my_list)



# create a menu
# going to put new things in and it will enable much better management

def menu():
    my_list_one = ["Mary", "Patsy", "Jean", "Constantine", "Pierre"]
    my_list_two = ["Bob", "Ron", "Max", "Joe", "Pat"]
    # assign one of the lists
    my_list = my_list_two
    # this simple print the list format is useful for testing sometimes
    print("my_list is currently set to : {}".format(my_list))
    my_menu = '''
            A: print the list
            B: print the list with indices
            C: add item to list
            D: print the value which is at a specific index number
            E: change value in the list
            F: choose list one
            G: choose list two
            H: Find item in list
            I: Remove item from List
            J: Sort list
            K: Shuffle list
            Q: Quit
            '''

# testing id
    #print(id(my_list_one))
    #print(id(my_list_two))
    #print(id(my_list))


    # call from inside the function where the list is
    # change_value(my_list)
    
    run = True
    while run == True:
        print(my_menu)
        choice = get_string("Please select your option: -> ").upper()
        print("."*100)
        if choice == "A":
            print_list(my_list)
        elif choice == "B":
            print_list_indexes(my_list)
        elif choice == "C":
            add_item(my_list)
        elif choice == "D":
            print_at_index(my_list)
        elif choice == "E":
            change_value(my_list)
        elif choice == "F":
            my_list = my_list_one
            print("my_list ONE is now selected")
        elif choice == "G":
            my_list = my_list_two
        elif choice == "H":
            find_item(my_list)
        elif choice == "I":
            remove_item(my_list)
        elif choice == "J":
            sort_list(my_list)
        elif choice == "K":
            shuffle_list(my_list) 
            print("my_list TWO is now selected")
        elif choice == "Q":
            print("Thank you")
        else:
            print("You have made an error")
            run = False
            
        
menu()

        
    
