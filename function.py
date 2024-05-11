import sys

def calculate_parameters(file_path, c=45):
    # Ensure c is within the valid range
    if not 25 <= c <= 100:
        raise ValueError("c must be between 25 and 100")

    # Open the file and read its contents
    with open(file_path, 'r') as file:
        input_string = file.read()

    # Replace spaces with zeros
    input_string = input_string.replace(' ', '0')

    # Calculate length of string
    length = 2541

    # Calculate remainder of length divided by c
    remainder = length % c

    # Calculate number of ampersands to add
    num_ampersands = c - remainder if remainder != 0 else 0

    # Add ampersands to the end of the string
    input_string += '&' * num_ampersands

    # Calculate number of rows
    num_rows = c

    # Calculate number of elements per row
    num_elements_per_row = (length + num_ampersands) // c

    return input_string, num_ampersands, num_rows, num_elements_per_row

def place_ampersands_in_array(input_string, num_rows, num_elements_per_row, num_ampersands):
    # Convert the string to a list of characters
    input_list = list(input_string)

    # Initialize an empty array
    array = [['' for _ in range(num_elements_per_row)] for _ in range(num_rows)]

    # Iterate over the array and fill it with characters from the list
    for i in range(num_rows):
        for j in range(num_elements_per_row):
            # If the number of ampersands left is equal to the number of rows left
            if num_ampersands == num_rows - i:
                # If this is the last element in the row
                if j == num_elements_per_row - 1:
                    # Place an ampersand here
                    array[i][j] = '&'
                    num_ampersands -= 1
                else:
                    # Otherwise, place the next character from the list here
                    array[i][j] = input_list.pop(0)
            else:
                # If the list is empty, fill the rest of the array with ampersands
                if not input_list:
                    array[i][j] = '&'
                    num_ampersands -= 1
                else:
                    # Otherwise, place the next character from the list here
                    array[i][j] = input_list.pop(0)

    return array

def transpose_and_extract_text(array):
    # Transpose the array
    transposed_array = list(map(list, zip(*array)))

    # Form a sentence from the transposed array
    sentence = ''
    for row in transposed_array:
        for element in row:
            if element == '0':
                sentence += ' '
            elif element != '&':
                sentence += element

    return sentence

def main():
    # Check if a file path was provided
    if len(sys.argv) < 2:
        print("Please provide a file path as a command-line argument.")
        return

    # Get the file path from the command-line arguments
    file_path = sys.argv[1]

    # Calculate parameters
    input_string, num_ampersands, num_rows, num_elements_per_row = calculate_parameters(file_path)

    # Print the results
    print(f"Modified string: {input_string}")
    print(f"Number of ampersands to add: {num_ampersands}")
    print(f"Number of rows: {num_rows}")
    print(f"Number of elements per row: {num_elements_per_row}")

    # Place ampersands in array
    array = place_ampersands_in_array(input_string, num_rows, num_elements_per_row, num_ampersands)

    # Print the array
    for row in array:
        print(row)

    # Transpose and extract text
    sentence = transpose_and_extract_text(array)

    # Print the sentence
    print("\nFormed sentence:")
    print(sentence)

if __name__ == "__main__":
    main()