from collections import deque

n_op = int(input())
my_deque = deque()

for i in range(n_op):
    input_str = str(input())
    split_input = input_str.split()
    
    input_command = getattr(my_deque, split_input[0])
    input_length = len(split_input)
    
    if input_length == 1:
        input_command()
    elif input_length == 2:
        input_value = int(split_input[1])
        input_command(input_value)
            
print(*my_deque, sep=" ")
