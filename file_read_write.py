
def modify_content(content):
    return content.upper()

try:
    input_filename = input("Enter the name of the file to read from: ")

    with open(input_filename, 'r') as infile:
        content = infile.read()

    modified_content = modify_content(content)

    output_filename = "modified_" + input_filename
    with open(output_filename, 'w') as outfile:
        outfile.write(modified_content)

    print(f"Success! Modified content written to '{output_filename}'.")

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' does not exist.")
except IOError:
    print(f"Error: Cannot read the file '{input_filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
