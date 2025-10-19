from colorama import Fore
import os
import sys

directory_path = sys.argv[1] if len(sys.argv)>=2 else "D:/Education/python/goit-pycore-hw-04"

def print_directroy(path_to_dir:str,tab_count:int):
    if path_to_dir[-1] != "/" and path_to_dir[-1] != "\\":
        path_to_dir += "/" 

    try:
        all_entries = os.listdir(path_to_dir)
        
        for entry in all_entries:
            full_path = os.path.join(path_to_dir, entry)
            if os.path.isfile(full_path):
                print(Fore.LIGHTGREEN_EX + "    "*tab_count+entry)
            elif os.path.isdir(full_path):
                print(Fore.LIGHTBLUE_EX + "    "*tab_count+entry)
                print_directroy(path_to_dir+entry+"/",tab_count+1)

    except FileNotFoundError:
        print(f"Error: Directory '{path_to_dir}' not found.")
    except NotADirectoryError:
        print(f"Error: '{path_to_dir}' is not a directory.")
    except PermissionError:
        print(f"Error: Permission denied to access '{path_to_dir}'.")

print(Fore.RESET)
print_directroy(directory_path,0)
print(Fore.RESET)