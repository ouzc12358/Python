game = [[1, 1, 1],
        [2, 2, 0],
        [1, 2, 0]]

#
def win(current_process):
    for rh in game:
        print(rh)
        if rh.count(rh[0]) == len(rh) and rh[0] != 0:
            print("Winner!")

win(game)