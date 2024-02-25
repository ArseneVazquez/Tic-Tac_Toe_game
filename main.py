grid = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]


def verify_victory(th_grid):
    for row in th_grid:
        if row[0] == row[1] == row[2] != " ":
            return True
    for column in range(3):
        if th_grid[0][column] == th_grid[1][column] == th_grid[2][column] != " ":
            return True
    if th_grid[0][0] == th_grid[1][1] == th_grid[2][2] != " ":
        return True
    if th_grid[0][2] == th_grid[1][1] == th_grid[2][0] != " ":
        return True
    return False


def show_grid(the_grid):
    for i in range(len(the_grid)):
        print("    |  ".join(the_grid[i]))
        if i != 2:
            print("-" * 20)


def play():
    player = 'X'

    while True:

        show_grid(grid)

        print("It's the player's turn", player)
        row = int(input("choose the row (0, 1, 2) : "))
        column = int(input("choose the column (0, 1, 2) : "))

        if (0 <= row < 3) and (0 <= column < 3) and (grid[row][column] == " "):
            grid[row][column] = player
            if verify_victory(grid):
                show_grid(grid)
                print(f"Congrats Player {player} You're the Winner 😍")
                break

            player = 'O' if player == 'X' else 'X'
            # if player == 'X':
            #     player = '0'
            # else:
            #     player = 'X'
        else:
            print("the case is invalid please choose another case")

        draw_match = True
        for row in grid:
            for column in row:
                if column != " ":
                    draw_match = False
                    break
            if not draw_match:
                break
        if draw_match:
            print('Its a Draw Match 🤝')


play()
