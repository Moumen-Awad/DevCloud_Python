import timeit
import os

def file_open_and_convert(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            value = line.strip()
            strings_array.append(value)
            #integers_array.append(convert_to_integer(value)) # Strip removes the newline character at the end of each line

def convert_to_integer(str):
    integer_value = 0
    string_length = len(str)
    for index, char in enumerate(str):
        reversed_index = string_length - 1 - index
        integer_value += char_tables["table_{}".format(reversed_index)][char]
    return integer_value

def insertion_sort(arr):
    # Traverse through the entire array starting from the second element
    element_sorted = 0
    
    for i in range(1, len(arr)):
        key = arr[i]  # Store the current element to be inserted
        j = i - 1  # Initialize a pointer to the previous element

        # Move elements of the sorted part of the array that are greater than the key
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key at its correct position in the sorted part of the array
        arr[j + 1] = key
        
        element_sorted += 1
    print(element_sorted)
        



if __name__ == "__main__":
    char_tables = {}
    for j in range(6):
        char_tables["table_{}".format(j)] = ({char: i*(27**j) for i, char in enumerate('abcdefghijklmnopqrstuvwxyz@')})

    strings_array = []
    integers_array = []
    
    file_open_and_convert(os.path.join(os.getcwd(), "data/million.txt"))


    execution_time1 = timeit.timeit(lambda: insertion_sort(strings_array), number=1)
    #execution_time2 = timeit.timeit(lambda: insertion_sort(integers_array), number=1)

    print("String: {} Seconds".format(execution_time1))
    #print("Integer: {} Seconds".format(execution_time2))
