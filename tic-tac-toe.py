def amount_x_o(list_):
    amount_x = 0
    amount_o = 0
    amount_ = 0
    for element in list_:
        if element == "X":
            amount_x += 1
        elif element == "O":
            amount_o += 1
        else:
            amount_ += 1
    return [amount_x, amount_o, amount_]





each_el = ["_" for n in range(9)]
global_counter = 1


print("""---------
| _ _ _ |
| _ _ _ |
| _ _ _ |
---------""")

while True:
    
    matrix = [[each_el[i], each_el[i + 1], each_el[i + 2]] for i in range(0, 9, 3)]
    amount_el = amount_x_o(each_el)
    vertical = [[matrix[j][0] for j in range(3)], [matrix[j][1] for j in range(3)], [matrix[j][2] for j in range(3)]]
    diag = [[matrix[i][i] for i in range(3)], [matrix[i][2 - i] for i in range(3)]]
    
    if (['X', 'X', 'X'] in matrix or
        ['X', 'X', 'X'] in vertical or
        ['X', 'X', 'X'] in diag):
        print("X wins")
        break
    elif (['O', 'O', 'O'] in matrix or
          ['O', 'O', 'O'] in vertical or
          ['O', 'O', 'O'] in diag):
        print("O wins")
        break
    elif amount_el[2] == 0:
        print("Draw")
        break

    if global_counter % 2 != 0:
        mark = "X"
    else:
        mark = "O"

    global_counter += 1
    
    y, x = input("Enter the coordinates: ").split()
    one_three = [1, 2, 3]
    counter = 0

    while counter == 0:
        if y.isalpha() or x.isalpha():
            print("You should enter numbers!")
            y, x = input("Enter the coordinates: ").split()
        elif int(y) not in one_three or int(x) not in one_three:
            print("Coordinates should be from 1 to 3!")
            y, x = input("Enter the coordinates: ").split()
        elif matrix[int(y) - 1][int(x) - 1] != "_":
            print("This cell is occupied! Choose another one!")
            y, x = input("Enter the coordinates: ").split()
        else:
            counter += 1

    each_el = [ each_el[n] if n != 3 * (int(y) - 1) + int(x) - 1 else mark for n in range(9)]
    cells = "".join(each_el)
    print("---------")
    print("|", cells[0], cells[1], cells[2], "|")
    print("|", cells[3], cells[4], cells[5], "|")
    print("|", cells[6], cells[7], cells[8], "|")
    print("---------")
