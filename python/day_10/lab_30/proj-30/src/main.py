from typing import TextIO

def read_file(file: TextIO) -> str:
    """
    Read a file and return its content.

    Args:
        filename (TextIO): The file object to read.
    """
    content = file.read()
        
    return content

def write_file(filename: str, content: str) -> None:
    """
    Append content to a file.

    Args:
        filename (str): The name of the file to write.
        content (str): The content to append to the file.
    """
    with open(filename, 'a') as file:
        file.write(content)

with open('../input/text.txt', 'r') as file:
    print(read_file(file))

write_file('output.txt', '\nHello, Again!')

with open('output.txt', 'r') as file:
    print(file.read())