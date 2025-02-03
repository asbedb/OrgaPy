# OrgaPy

OrgaPy is a command-line file organization tool that helps you manage and analyze your files and directories. It provides basic file system navigation, file analysis, and automatic file sorting capabilities.

## Features

- Directory navigation and file system exploration
- File system analysis (file count and total size)
- Automatic file sorting by extension
- Cross-platform compatibility (Windows, Linux, and macOS)

## Commands

- `ls` - List all files and directories in the current working directory
- `cd <path>` - Change current working directory
  - Use `cd ..` to navigate to parent directory
  - Use `cd` without arguments to show current directory
- `clear` or `cls` - Clear the console screen
- `analyze` - Calculate total file count and size in the current directory
- `sort` - Organize files into folders based on their extensions
- `help` - Display available commands
- `exit` - Exit the program

## File Sorting

The `sort` command creates folders based on file extensions and moves files into their respective folders. For example:
- A file named `document.pdf` will be moved to a `pdf` folder
- A file named `image.jpg` will be moved to a `jpg` folder

**Warning**: The sort operation is irreversible. The program will ask for confirmation before proceeding.

## Usage

1. Run the script using Python:
```bash
python orgapy.py
```

2. Set your working directory using the `cd` command:
```bash
OrgaPy C:\> cd Documents
```

3. Use the available commands to manage and organize your files.

## System Requirements

- Python 3.x
- Standard Python libraries (no additional installations required):
  - `os`
  - `shutil`
  - `platform`

## To Do

Future improvements planned:
- Implement revert option for sorting operations
- Add command history functionality
- Include additional file analysis features (e.g., old files identification)

## Notes

- The program starts in the root directory of where you have placed the file
- All operations are performed in the current working directory
- Exercise caution when using the sort function as it modifies your file system structure