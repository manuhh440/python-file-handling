import os

def read_file(filename):
    """
    Reads the content of a file.

    Args:
        filename (str): The name of the file to read.

    Returns:
        str: The content of the file, or None if an error occurs.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: File not found - {filename}")
        return None
    except IOError:
        print(f"Error: Could not read file - {filename}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        return None

def write_file(filename, content):
    """
    Writes content to a file.

    Args:
        filename (str): The name of the file to write to.
        content (str): The content to write to the file.

    Returns:
        bool: True if the write was successful, False otherwise.
    """
    try:
        with open(filename, 'w') as file:
            file.write(content)
        return True
    except IOError:
        print(f"Error: Could not write to file - {filename}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred while writing to the file: {e}")
        return False

def modify_content(content):
    """
    Modifies the content read from the file.
    This function adds a line to the beginning and end of the file

    Args:
        content (str): The original content of the file.

    Returns:
        str: The modified content.
    """
    modified_content = "Start of modified content\n" + content + "\nEnd of modified content"
    return modified_content

def process_file(input_filename, output_filename):
    """
    Reads, modifies, and writes file content, handling potential errors.

    Args:
        input_filename (str): The name of the input file.
        output_filename (str): The name of the output file.
    """
    content = read_file(input_filename)
    if content is None:
        print("Operation aborted due to reading error.")
        return  # Stop if there was an error reading.

    modified_content = modify_content(content)
    if write_file(output_filename, modified_content):
        print(f"Successfully wrote modified content to {output_filename}")
    else:
        print("Operation aborted due to writing error.")

def get_valid_filename(prompt, file_exists_check=False):
    """
    Gets a valid filename from the user, with input validation and optional file existence check.

    Args:
        prompt (str): The prompt to display to the user.
        file_exists_check (bool, optional): If True, check if the file exists. Defaults to False.

    Returns:
        str: The valid filename entered by the user, or None if the user cancels.
    """
    while True:
        filename = input(prompt).strip()
        if not filename:
            print("Filename cannot be empty. Please try again.")
            continue

        if file_exists_check and not os.path.exists(filename):
            print(f"Error: File '{filename}' does not exist.  Please enter an existing file.")
            continue

        # Basic filename validation (optional, more robust checks can be added if needed)
        if any(char in filename for char in r'<>:"/\|?*'):
            print("Invalid characters in filename. Please use a valid filename.")
            continue

        return filename

def main():
    """
    Main function to coordinate the file processing.
    Gets input and output filenames from the user and calls process_file.
    """
    input_filename = get_valid_filename("Enter the name of the input file: ", file_exists_check=True)
    output_filename = get_valid_filename("Enter the name of the output file: ")
    process_file(input_filename, output_filename)

if __name__ == "__main__":
    main()

