import os

# asks the user for a directory
def get_input():
    return input("Please enter the directory to sort: ")

def sort(path):
    # get the files
    files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))] 
    # loop over files
    for file in files:
        full_path = os.path.join(path, file) # creates a path to the file
        if "." in file:
            new_dir = os.path.join(path, os.path.splitext(file)[1][1:]) # creates a directory with the files extention
            move_file_into_directory(new_dir, path, full_path, file) # moves the file into the new directory
        else:
            new_dir = os.path.join(path, "no_extention") # creates a directory called no_extention for files without
            move_file_into_directory(new_dir, path, full_path, file) # moves the file into the new directory

def move_file_into_directory(new_dir, path, full_path, file):
    # checks if the new directory exists and ensures it is a directory
    if os.path.exists(new_dir) and os.path.isdir(new_dir):
        new_file = os.path.join(path, new_dir, file)
        os.rename(full_path, new_file) # moves the file into the directory
        print("Moved file: %s" % new_file)
    else:
        try:
            os.mkdir(new_dir) # create the directory
            new_file = os.path.join(path, new_dir, file)
            os.rename(full_path, new_file) # moves the file into the directory
            print("Moved file: %s" % new_file)
        except OSError:
            print("Failed to make directory %s" % new_dir) # failed to make directory


if __name__ == "__main__":
    dir = get_input()
    sort(dir)