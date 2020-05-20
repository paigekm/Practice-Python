def get_integer(m):
    my_integer = int(input(m))
    return my_integer


def get_string(m):
    my_string = input(m)
    return my_string


def add_name_age(N, A):
    # create a loop so you can add multiple people to the list
    # loop x number of times
    count = get_integer("How many people would you like to add?")
    for i in range(0, count):
        name = get_string("Please enter name: ->")
        age = get_integer("Please enter age: ->")
        # N and A correspond
        N.append(name)
        A.append(age)


# N and A are being sent into it
def review(N, A):
    # checking the two lists you are pairing are the same length
    # safety check to ensure you can go
    if len(N) == len(A):
        for i in range(0, len(N)):
            # format(N,A) we use N and A because the function cannot access 'N' and 'A'
            # so they have to be sent
            # i is effectively the counter so it is printing the name at each index (represented by i)
            output = "{} is {} years old".format(N[i],A[i])
            print(output)
    else:
        print("Lists do not have the same number of elements in them, so we can't continue")


def menu():
    name=[]
    age=[]
    my_menu= '''
    A: Add names and ages
    R: Review
    Q: Quit
    '''
    run = True
    while run == True:
        print(my_menu)
        # .upper() changes the entry's case to uppercase immediately so it is recognisable
        choice = get_string("Please choose an action to do: -> ").upper()
        if choice == "A":
            # this has to get the arguments N and A
            add_name_age(name, age)
        elif choice == "R":
            review(name, age)
        elif choice == "Q":
            print("Thank you")
            run = False
        else:
            print("You have made an error")
        print("."*100)


menu()