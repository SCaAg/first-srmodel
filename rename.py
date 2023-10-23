import os

# Specify the directory containing the files to be renamed
directory = './.div2k/images/DIV2K_valid_HR'  # Change this to your directory path

# List all files in the directory
files = os.listdir(directory)

# Initialize a counter for numbering
counter = 66852



# Loop through the files and rename them
for filename in files:
    # Construct the new filename using a 4-digit number
    new_filename = f'{counter:06}.png'
    
    # Full path of the original file
    old_path = os.path.join(directory, filename)
    
    # Full path of the new file
    new_path = os.path.join(directory, new_filename)
    
    # Rename the file
    os.rename(old_path, new_path)
    
    # Increment the counter for the next file
    counter += 1