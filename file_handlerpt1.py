# problem 4- file handling


def process():
    # open integers.txt (read), double.txt(append), triple.txt (append)
    with open("integers.txt") as input_file, open("double.txt", "a") as output_even_file, open("triple.txt", "a") as output_odd_file: 
    # read integers.txt    
        for line in input_file:
            input_num = int(line)
            # if even integers
            if input_num % 2 == 0:
                #get the square
                square = input_num * input_num

    # write to double.txt
    #else
    # if odd integers
    #  get the cube 
    # write to triple.txt