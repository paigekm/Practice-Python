# look at different ways we can make a loop
# this is a notes file of examples everything working in functions



# FIRST UP
# loop with a counter (will run a certain number of times)
def loop_with_counter(n):
    # n means it is expecting to recieve one value from when the function is called somewhere in the program
    # give it a starting number
    c = 0
    # condition of the loop
    # this is where we use n
    while c < n:
        # put spaces around phrases to make it more clear
        print(   "hello c is now {}".format(c)   )
        # increment c
        # works right to left in terms of the c=1 if the second c is 0
        # c = c + 1 can be written as
        c += 1
    return None




# SECOND example of loop
# indefinite loop
# if waiting to get input, don't know when we want to stop it
# someone has to enter value to stop the loop
def indefinite_loop():
    # variable it needs to stop
    run = True
    while run == True:
        # get input from the user
        user_choice = input("Press 'n' to stop the loop\n or anything else to stay in it: ->")
        if user_choice == "n":
            # stops the loop
            print("Loop will stop")
            run = False
        else:
            # will stay in the loop
            print("You are still in the loop")



# THIRD kind of loop
# often called a for loop
# similar but more efficient than the 1st loop (count and while loop)
def for_in_range_loop():

    # this has a built in counter
    # can be anything but we generally use i or j or k (conventions)
    # can add steps (if no step, assumes step is one)
        # it requires an integer (not a decimal) for the step
    
    # have a start and a finish value in the brackets,
    # starts iterating at 3 and ends at 19 (20 is not included)
    # i is the counter - i contains the count values from 3 up to 19
    # 5 is the defined step value, the amount it goes/jumps up by each time
    for i in range(3, 20, 5):
        print(i)


# FOURTH loop
# double loop
def double_loop():
    # the i runs 6 times
    # the i in 'range' loop runs once
    # first counter for i is 0
    for i in range(0,6):
        # the j runs 7 times (0-6)
        # the i goes to 1 (the next one)
        # it runs 7 times again
        # you get 42 (6*7) iterations out of it
        for j in range(0,7):
            # end means it prints each j loop across the page not down
            # prints a new line after each j loop
            # with j and i in the correct order, you can print a coordinates system
            # with double loops can start to manage how things appear on a grid
            # manage things/objects in a grid system, things sitting on a grid with co-ordinates
            # double loop has huge applications when making systems more complex
            # like in game design etc.
            print( "({} , {})".format(j,i), end = "" )
        print()


def menu():
    my_menu = '''
                1: while loop with counter
                2: while loop with quit
                3: for in range
                4: double loop
                0: quit
                '''
    print(my_menu)
    choice = int(input("choose your option: -> "))
    if choice is 1:
        amount = int(input("How many would you like: -> "))
        # when drawing amount from other place in program
        loop_with_counter(amount)
    elif choice is 2:
        indefinite_loop()
    elif choice is 3:
        for_in_range_loop()
    elif choice is 4:
        double_loop()
    elif choice is 5:
       print("Thank you") 
        



# CALLING THE FUNCTIONS
#for a test you can actually write the number, just testing
#loop_with_counter(6)
#indefinite_loop()
#for_in_range_loop()
#double_loop()
menu()

