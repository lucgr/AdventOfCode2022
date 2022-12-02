def method():
    file = open('input2.txt', 'r')
    sum = 0
    # for line in file:
    #     opponent = find_move_opponent(line.split()[0])
    #     you = find_move_you(line.split()[1])
    #     sum += find_score(opponent=opponent, you=you)
    for line in file:
        opponent = find_move_opponent(line.split()[0])
        you = find_move_you_part2(opponent=opponent, you=line.split()[1])
        sum += you #find_score(opponent=opponent, you=you)
    print(sum)

def find_move_opponent(input: str):
    match input:
        case "A":
            return 1
        case "B":
            return 2
        case "C":
            return 3

def find_move_you(input: str):
    match input:
        case "X":
            return 1
        case "Y":
            return 2
        case "Z":
            return 3

def find_move_you_part2(opponent: int, you: str):
    match you:
        case "X": # lose
            move = 1 + ((opponent + 1) % 3)
            return move
        case "Y": # draw
            move = opponent
            return move + 3
        case "Z": # win
            move = 1 + (opponent % 3)
            return move + 6

def find_score(opponent: int, you: int):
    if opponent == you:
        return 3 + you # return a draw plus the value of your move
    elif (opponent, you) in [(1, 3), (2, 1), (3, 2)]:
        return you # return a loss (zero) plus the value of your move
    else:
        return 6 + you # return a win (six) plus the value of your move


if __name__ == '__main__':
    method()