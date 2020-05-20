def add_names_age(N,A):
    run = True
    while run == True:
        name = get_string
        age = get_string
        N.append(name)
        A.append(age)
        run = False


def review(N,A):
    if len(N) == len(A):
        for in range (0, 20)
    else:
        print("Lists are not the same size")

def menu():
    name = []
    age = []
    my_menu = '''
            A: Add
            R: Review
            Q: Quit
            '''
    run = True
    while run == True:
        print(my_menu)
        choice = get_string("Please select your menu option: -> ").upper()
        print("."*100)
        if choice == "A":
            add_names_age(my_list)
        elif choice == "R":
            review(my_list)
        elif choice == "Q":
            print("Thank you")

menu()
