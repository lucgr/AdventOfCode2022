def method():
    file = open('input1.txt', 'r')
    sum_one = 0
    highest_sum = 0
    second_sum = 0
    third_sum = 0
    for line in file:
        if len(line.split()) == 0:
            if sum_one > highest_sum:
                third_sum = second_sum
                second_sum = highest_sum
                highest_sum = sum_one
            elif sum_one > second_sum:
                third_sum = second_sum
                second_sum = sum_one
            elif sum_one > third_sum:
                third_sum = sum_one
            sum_one = 0
        else:
            sum_one += int(line.split()[0])
    print("Highest sum: "+ str(highest_sum))
    print("Second highest: "+ str(second_sum))
    print("Third highest: "+ str(third_sum))
    print(highest_sum + second_sum + third_sum)


if __name__ == '__main__':
    method()
