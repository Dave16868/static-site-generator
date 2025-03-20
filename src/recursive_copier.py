import os
import shutil

def recursive_copier(from_path, to_path):
    print(f"checking if file {from_path} exists...")
    if os.path.exists(f"{from_path}"):
        print(f"it exists! creating list of what's inside...")
        list_to_copy = os.listdir(from_path)
        print(f"list of things to copy: {list_to_copy}")
        for item in list_to_copy:
            item_path = os.path.join(f"{from_path}", item)
            copy_path = os.path.join(f"{to_path}", item)
            print(f"checking if {item_path} is a file or directory...")
            is_file = os.path.isfile(item_path)
            if is_file:
                print(f"its a file! copying over to {copy_path}")
                shutil.copy(item_path, copy_path)
            if not is_file: 
                print(f"its a directory! calling this function again with from_path: {item_path} and to_path: {copy_path}")
                os.mkdir(copy_path)
                recursive_copier(item_path, copy_path)
        print(f"Finished copying everything from this directory: {from_path} into {to_path}")
    else:
        raise FileNotFoundError("input path specified not found!")

# check if list is a file
# if is a file, copy to to_path, if not, its a dir. join from_path and to_path with dir name and call func again
# func will recursively call and join path name until find a file, and copy to to_path, then return