def adding(a,b):
    my_sum = a+b
    #make a string
    my_string = "{}+{}={}".format(a,b,my_sum)
    print(my_string)

def subtracting(a,b):
    my_sum = a-b
    my_string = "{}-{}={}".format(a,b,my_sum)
    print(my_string)

def multiplying(a,b):
    my_sum = a*b
    my_string = "{}x{}={}".format(a,b,my_sum)
    print(my_string)

def dividing(a,b):
    my_sum = a/b
    my_string = "{}/{}={}".format(a,b,my_sum)
    print(my_string)

#adding(3,5)
#subtracting(5,6)
#multiplying(2,2)
#dividing(4,2)




    
#puts info into box
#m stands for message and allows
#you to print different messages at different places in the program

def get_integer(m):
    my_number = int(input(m))
    return my_number
    
#draws info out of box and prints menu
def menu():
    num_one = get_integer("Please enter your first number, then press enter:")
    num_two = get_integer("Please enter your second number, then press enter:")
    my_menu = '''
        1: add
        2: subtract
        3: multiply
        4: divide
        0: quit
        '''
    print(my_menu)
    choice = get_integer("Please choose an option from the above menu:")
    if choice == 1:
        adding(num_one, num_two)
    elif choice == 2:
        subtracting(num_one, num_two)
    elif choice == 3:
        multiplying(num_one, num_two)
    elif choice == 4:
        dividing(num_one, num_two)
    elif choice == 0:
        print("Quitting")
    else:
        print("Unrecognised entry")

menu()      


