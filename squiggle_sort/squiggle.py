def make_squiggle(vert, hor):
    counter = 1
    curr_vert = 0
    curr_hor = 0
    old_vert = 0
    old_hor = 0
    matrix = [[0 for x in range(hor)] for y in range(vert)]

    while counter <= vert * hor:
        matrix[curr_vert][curr_hor] = counter
        if (curr_vert - 1 < 0) or (curr_hor + 1 >= hor):
            if old_vert + 1 >= vert:
                old_hor += 1
                curr_vert = old_vert
                curr_hor = old_hor
            else:
                old_vert += 1
                curr_vert = old_vert
                curr_hor = 0
            counter += 1
        else:
            curr_vert -= 1
            curr_hor += 1
            counter += 1

    for row in matrix:
        print(row)

make_squiggle(5, 6)

