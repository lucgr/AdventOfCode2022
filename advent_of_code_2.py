def method():
    file = open("input/input2.txt", "r")
    sum1 = 0
    sum2 = 0
    for line in file:
        opponent = find_move(line.split()[0])
        you = find_move(line.split()[1])
        sum1 += find_score(opponent=opponent, you=you)
        you_new_strat = find_move_strategy(opponent=opponent, you=line.split()[1])
        sum2 += you_new_strat
    print(f"Part 1 - Sum: {sum1}")
    print(f"Part 2 - Sum: {sum2}")


def find_move(input: str):
    if input in ["A", "X"]:
        return 1
    elif input in ["B", "Y"]:
        return 2
    else:
        return 3


def find_move_strategy(opponent: int, you: str):
    match you:
        case "X":  # lose
            return 1 + ((opponent + 1) % 3)
        case "Y":  # draw
            return opponent + 3
        case "Z":  # win
            return 7 + (opponent % 3)


def find_score(opponent: int, you: int):
    if opponent == you:
        return 3 + you  # return a draw plus the value of your move
    elif (opponent, you) in [(1, 3), (2, 1), (3, 2)]:
        return you  # return a loss (zero) plus the value of your move
    else:
        return 6 + you  # return a win (six) plus the value of your move


if __name__ == "__main__":
    method()
