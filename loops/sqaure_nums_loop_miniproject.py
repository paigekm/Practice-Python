# going to use the in range loop

def square_num(n):
    for i in range(0,n):
        my_square = i*i
        my_output = "{} squared = {}".format(i,my_square)
        print(my_output)
    print()

#square_num(20)
#square_num(1000)

def cube_num(n):
    for i in range(0,n):
        my_cube = i*i*i
        my_output = "{} cubed = {}".format(i,my_cube)
        print(my_output)
    print()

#cube_num(15)



def menu():
    # putting menu into a loop
    # define a variable to stop or start the loop (run is this variable)
    run = True
    while run == True:
        my_menu = '''
                    A: Square Numbers
                    B: Cube Numbers
                    Q: Quit
                    '''
        print("Welcome!")
        print(my_menu)
        choice = input("Please choose an option")
        if choice == "A":
            square_num(6)
        elif choice == "B":
            cube_num(11)
        elif choice == "Q":
            # leaving the loop when you want to quit
            run = False
            print("Thanks for squaring and cubing!")
        else:
            print("Invalid entry")

menu()
