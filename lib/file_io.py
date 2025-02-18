
def write_file(file_name, file_content):
    """Writes content to a file, overwriting it if it exists."""
    with open(f"{file_name}.txt", "w") as file:
        file.write(file_content)

def append_file(file_name, append_content):
    """Appends content to a file."""
    with open(f"{file_name}.txt", "a") as file:
        file.write(append_content)

def read_file(file_name):
    """Reads the content of a file and returns it."""
    with open(f"{file_name}.txt", "r") as file:
        return file.read()

write_file(file_name="logfile", file_content="Log 1: 5 bananas added\n")
append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted\n")
print(read_file(file_name="logfile"))
