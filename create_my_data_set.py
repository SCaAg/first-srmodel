from PIL import Image,ImageFilter
import random
import numpy as np
import os

# Specify the directory containing the files to be renamed
directory = './.div2k/images/DIV2K_valid_HR'  # Change this to your directory path
save_dirctory = './.div2k/images/DIV2K_valid_LR_bicubic/X2'
# List all files in the directory
files = os.listdir(directory)


scaling_factor=2



os.makedirs(save_dirctory, exist_ok=True)




def my_convert(img):
    img_dir=os.path.join(directory,img)
    hr_img=Image.open(img_dir)
    img_array=np.array(hr_img)
    img_array=img_array/255*15
    img_array=img_array+0.5
    img_array=img_array.astype(np.uint8)
    img_array=img_array/15*255
    img_array=img_array
    img_array=img_array.astype(np.uint8)
    hr_img=Image.fromarray(img_array)
    lr_img = hr_img
    blur = random.choice([True, False])
    resize = random.choice(
        ["bicubic", "bilinear", "nearest", "lanczos", "box", "hamming"])
    noise = random.choice(["gauss", "poisson", "none"])

    try:
        # Blur
        if blur:
            lr_img.filter(ImageFilter.GaussianBlur(
                radius=1))

        l_width = int(hr_img.width / scaling_factor)
        l_height = int(hr_img.height / scaling_factor)

        # Noise
        if noise == "gauss":
            mean = 0
            std = 0.1
            gauss_noise = np.random.normal(
                mean, std, (lr_img.height, lr_img.width, 3)).astype(np.uint8)
            lr_img = np.add(lr_img, gauss_noise)
            lr_img = Image.fromarray(lr_img)
        elif noise == "poisson":
            lam = 0.1
            poisson_noise = np.random.poisson(
                lam, (lr_img.height, lr_img.width, 3)).astype(np.uint8)
            lr_img = np.add(lr_img, poisson_noise)
            lr_img = Image.fromarray(lr_img)
    except Exception as e:
        print(f"An error occurred:{e}")
    # Downsize
    if resize == 'bicubic':
        lr_img = lr_img.resize((l_width, l_height), Image.BICUBIC)
    elif resize == 'bilinear':
        lr_img = lr_img.resize((l_width, l_height), Image.BILINEAR)
    elif resize == 'nearest':
        lr_img = lr_img.resize((l_width, l_height), Image.NEAREST)
    elif resize == 'lanczos':
        lr_img = lr_img.resize((l_width, l_height), Image.LANCZOS)
    elif resize == 'box':
        lr_img = lr_img.resize((l_width, l_height), Image.BOX)
    else:
        lr_img = lr_img.resize((l_width, l_height), Image.HAMMING)



    # Sanity check
    if hr_img.width == lr_img.width * scaling_factor and hr_img.height == lr_img.height * scaling_factor:
        pass
    else:
        print(img,"is not right")

    img=img[:-4]
    img=img+"x2.png"

    
    lr_img.save(os.path.join(save_dirctory,img))

my_convert(files[3])
count=0
for img in files:
    my_convert(img)
    count+=1
    if count % 1000==0:
        print(f"finish{count}")