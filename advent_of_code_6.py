def method():
    file = open("input/input6.txt", "r")
    sequence = str(file.read())
    ### PART 1 ###
    find_start(sequence, 4)

    ### PART 2 ###
    find_start(sequence, 14)

def find_start(sequence, length):
    for i in range(0, len(sequence)):
        set_length = set(sequence[i:i+length])
        if len(set_length) == length:
            print(i + length)
            return

if __name__ == "__main__":
    method()