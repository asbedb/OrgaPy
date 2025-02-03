import os
import shutil
import platform

root_dir = os.path.abspath(os.sep)
working_dir = os.getcwd() 
#to do list - revert option, history, additional analysis (old files etc)

def clear_console():
    system_name = platform.system().lower()
    if system_name == 'windows':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Linux and macOS

def list_content():
    contents = os.listdir(working_dir)
    for item in contents:
        print(item)  # Print each item in the directory

def set_working_dir(path_parts: str):
    global working_dir
    print(working_dir)
    if not path_parts:  # If no path parts are provided, print the current directory
        print(f'Current Directory: {working_dir}')
    else:
        if path_parts == [".."]:  # Check if the user wants to go back a directory
            working_dir = os.path.abspath(os.path.join(working_dir, os.pardir))  # Parent directory
            print(f"Changed directory to {working_dir}")
        else:
            new_dir = os.path.join(working_dir, *path_parts)  # Combine current path with input path parts
            if os.path.isdir(new_dir):  # Check if the new directory exists
                os.chdir(new_dir) 
                working_dir = new_dir
                print(f"Changed directory to {working_dir}")
            else:
                print(f"Directory not found: {new_dir}")

def analyze():
    total_size = 0
    file_count = 0
    print(f'Analysis has begun - this may take a few minutes')
    for dirpath, dirnames, filenames in os.walk(working_dir):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if os.path.isfile(filepath):
                file_count+=1
                total_size += os.path.getsize(filepath)
    
    print(f"Number of files: {file_count}")
    # Convert total size from bytes to MB
    total_size_mb = total_size / (1024 * 1024)
    # If the size exceeds 1000 MB, convert to GB and show the remainder in MB
    if total_size_mb >= 1000:
        total_size_gb = total_size_mb // 1024  # Integer division for GB
        remaining_mb = total_size_mb % 1024  # Remainder in MB
        print(f"Total size: {total_size_gb} GB and {remaining_mb:.2f} MB")
    else:
        print(f"Total size: {total_size_mb:.2f} MB")
    
def sort():
    print(f'You are about to sort the files in {working_dir}. This will organize all files by their extension into corresponding folders (e.g., "pdf/file.pdf").')
    # Ask for confirmation to proceed
    user_confirmation = input('Are you sure you want to proceed? This action is irreversible. (y/n): ').lower()
    if user_confirmation in ['y', 'yes']:
        print("Proceeding with sorting...")
        for _, _, filenames in os.walk(working_dir):
            for filename in filenames:
                # Get the file extension
                _, file_extension = os.path.splitext(filename)   
                if file_extension:
                    file_extension_without_period = file_extension.lstrip('.')
                    folder_name = file_extension_without_period  # Specify your folder name
                    # Combine the current working directory with the folder name
                    folder_path = os.path.join(working_dir, folder_name)
                    # Create the folder (if it doesn't exist)
                    os.makedirs(folder_path, exist_ok=True)
                    # Construct the full file path
                    file_path = os.path.join(working_dir, filename)
                    if os.path.exists(file_path):
                        # Move the file to the respective folder
                        destination_path = os.path.join(folder_path, filename)
                        shutil.move(file_path, destination_path)  # Move the file
                    
        print(f'Folders Created/Updated and Files Sorted')


    elif user_confirmation in ['n','no']:
        print("Action canceled. No files were sorted.")
    else:
        print("Invalid Prompt please try again.")

def run():
    print(f'Set your drive:')
    while True:
        user_input = input(f'OrgaPy {working_dir}> ')
        match user_input.split():
            case ["ls"]:
                list_content()
            case ["clear"] | ["cls"]:
                clear_console()
            case ["cd", *path_parts]:
                set_working_dir(path_parts)
            case ["exit"]:
                print("Exiting...")
                break  # Exit the loop when the user types "exit"
            case["analyze"]:
                analyze()
            case["sort"]:
                sort()
            case ["help"]:
                print(
                    f'---------------------------'
                    f'\nList of Commands:\n\n'
                    f'ls - List files in the current directory\n'
                    f'clear - Clear the console\n'
                    f'exit - Exit the program\n'
                    f'cd <path> - Change to the specified directory (without a path shows the current directory)\n'
                    f'---------------------------'
                )
            case _:
                print(f"Unrecognized command: {user_input}")
    


run()