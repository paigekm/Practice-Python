# always have these two functions in your programs
# functions used to get integers or string information from the user
# consider these will be expanded on
# but these will be placeholder functions we use and refer to regularly

def get_integer(m):
    my_integer = int(input(m))
    return my_integer

def get_string(m):
    my_string = input(m)
    return my_string

# these two function above always include them!!!



my_list = ["Mary", "Patsy", "Jean", "Constantine", "Pierre"]
#print (len(my_list))

# accessing an item at an index
# find the item at index number 2
print(my_list [2])
# gives jean

print(my_list[7])
# program crash (list index out of range) because this item doesn't exist
# no seventh item in the list


# design a function to get something at a particular index
# list gets carried from some other  part of the program
# need a holder/argument which is L which means a list is being passed into the function

def print_at_index(L):
    my_index = get_integer("please choose index")
    # print what is at that index
    # list coming in is L
    # [] acessing an item at an index,
    # don't know what it will be but the variable my_index is holding it
    print (L[my_index])
# ask the user for an index number then print out what is in the list 
print_at_index(my_list)




# function for printing things out

def print_list(L):
    # print(L)
    # will print exactly what the list looks like [Mary, ...]
# can use the above for testing, a brief look at the list
# standard way to print out the list using a loop
    for x in L:
        # x will take the value of each item in the list
        print(x)
        # this will print out the list of names

# print out list with the index numbers too
# need menu structure, use with lists
# use indexes as the option numbers in a menu
def print_list_indexes(L):
    # first index value in the list is 0
    # in range counts up to every number except the last number
    # len(L) guarantees go up end of list and no further
    for i in range(0, len(L)):
        # i counter in the index number, loops through 0,1,2,3,4
        # L[i] prints the value at the index
        print ("{} : {}".format(i,L[i])
# example of a test
print_list_indexes(my_list)




#adding something to a list
# python method my_list.append("Damian")
               # the list now has damian in the list
def add_item(L):
            added_item = get_string("Please enter new item")
            # L is the placeholder for whatever is being passed
            L.append(added_item)
# call this
add_item(my_list)

    
               

        
 

 
