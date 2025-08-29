try:
    # Get filename from user
    input_filename = input("Enter the input filename: ")
    
    # Read the input file
    with open(input_filename, 'r') as input_file:
        content = input_file.read()
    
    # Modify content (example: convert to uppercase)
    modified_content = content.upper()
    
    # Create output filename
    output_filename = f"modified_{input_filename}"
    
    # Write to new file
    with open(output_filename, 'w') as output_file:
        output_file.write(modified_content)
    
    print(f"File successfully processed and saved as {output_filename}")

except FileNotFoundError:
    print("Error: The specified file does not exist.")
except PermissionError:
    print("Error: Permission denied when accessing the file.")
except IOError:
    print("ErroriomaError: An error occurred while reading or writing the file.")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")