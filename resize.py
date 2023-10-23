from PIL import Image
import os

# Specify the directory containing your images
input_directory = './.div2k/images/DIV2K_train_HR'

# Specify the directory to save the resized images
output_directory = './.div2k/images/DIV2K_train_HR'

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

count = 0

# Loop through all files in the input directory
for image_dir in os.listdir(input_directory):
    resize_image = Image.open(os.path.join(input_directory, image_dir))
    width, height = resize_image.size

    if width % 2 == 1 or height % 2 == 1:
        print('sdf')