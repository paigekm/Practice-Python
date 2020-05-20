# test file

def double_loop_print():
    for i in range(0, len(L)):
        output = "{}:{}".format(i, L[i])
        print(output)
        for j in range(0,len(L[i])):
            output = "{}:{}".format(j,L[i][j])
            print(output)


def main():
    class_list=[["Nia","Blond","16"],
             ["Tommi","Blond","16"],
             ["Grace","Brown","16"],
             ["Rebecca","Black","16"],
             ["Paige","Brown","16"]
    ]
    #print(class_list)
    #double_loop_print(class_list)
    for i in range(0,len(class_list)):
        # creates column structure
        # < or > makes right/left align
        output = "{:10} --- {:^10} --- {:<10}".format(class_list[i][0], class_list[i][1], class_list[i][2])
        print(output)


main()