from PIL import Image
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import resize
import cv2
from skimage.util import img_as_ubyte
from skimage import color


# TO DO:
# 1. make the pythagoras function/match the average rgbs, return the filename of the matching source image
# 2. resize the matching source image to the size of the square_pixel
#       img = resize(my_image, (square_pixel,square_pixel), anti_aliasing=True)
# 3. paste the image into the location of the pic
# 4. DONE ABOVE!! Now just need to refine some things

def main():
    # change this value to affect the size of the photomosaic section! NOTE: smaller size will take longer to render
    square_pixel = 10
    # NOTE: change this string to the name of the file .jpg in the project folder!
    my_image = io.imread('rsz_img_6638.jpg')

    # NOTE: this is the directory of the source images folder. Future, will let person decide which dir
    photo_dir= './small_photoset/*jpg'
    # dictionary where the keys are the filenames of the source images, and the values are the loaded source_image
    source_images = {}
    # dictionary where the keys are the filenames of the source images, and the values are the average rgb values
    source_image_avg_rgb_dict = {}
   
    image_collection = io.imread_collection(photo_dir)
    for filepath in image_collection.files:
        filename = filepath
        source_image = io.imread(filepath)
        # crop to square:
        source_images[filename] = square_source_images(source_image)
        img = square_source_images(source_image)
        source_image_avg_rgb_dict[filename] = calculate_average_colour(img)

    # this will allow for all the "pixel" squares to fit equally in the frame
    trim_rows = my_image.shape[0] % square_pixel
    trim_columns = my_image.shape[1] % square_pixel
    print(my_image.shape)

    my_image = my_image[0:my_image.shape[0]-trim_rows, 0:my_image.shape[1]-trim_columns]
    print(my_image.shape)

    row = []
    temporary_img = []

    for i in range(0, my_image.shape[0], square_pixel):
        for j in range(0, my_image.shape[1], square_pixel):

            pixel_region = my_image[i:i+square_pixel, j:j+square_pixel]
            pixel_colour = calculate_average_colour(pixel_region)

            best_match = match_colour(pixel_colour, source_image_avg_rgb_dict)

            img = io.imread(best_match)
            img = resize(img, (square_pixel,square_pixel), anti_aliasing=True)

            # the commented code below can give you a picture where the pixels are the average colour!
            # my_image[i:i+square_pixel, j:j+square_pixel] = pixel_colour
            
            row.append(img)
        temporary_img.append(np.hstack(row))
        row = []
    photomosaic = np.vstack(temporary_img)  

    # converts image to uint8 to suppress the warning that there's lossy conversion
    photomosaic=img_as_ubyte(photomosaic)

    # NOTE: change string to the name of the photomosaic you want to save! Future: will set this as an arg
    io.imsave('me_3.jpg', photomosaic)


def calculate_average_colour(pixel_region):
    # list turns [1 2 3] to [1, 2, 3] so that I can match avg rgb colours easier
    return(list(np.mean(pixel_region, axis =(0,1))))

# 
def match_colour(pixel_colour, source_image_avg_rgb_dict):
    smallest_distance = None
    best_match = None
    for filename in source_image_avg_rgb_dict:
        distance = (pixel_colour[0] - source_image_avg_rgb_dict[filename][0])**2 + (pixel_colour[1] - source_image_avg_rgb_dict[filename][1])**2 + (pixel_colour[2] - source_image_avg_rgb_dict[filename][2])**2
        if smallest_distance == None or distance < smallest_distance:
            smallest_distance = distance
            best_match = filename
    
    return best_match
        

def square_source_images(source_img):
    # crop on the smaller, e.g. if 1280 * 800 pixels, crop to 800 * 800
    # if more rows than columns
    if source_img.shape[0] > source_img.shape[1]:
        crop = source_img.shape[0] - source_img.shape[1]
        new_height = source_img.shape[0] - crop
        source_img = source_img[0:new_height,:]
        return source_img 
    else: # if more columns than rows
        crop = source_img.shape[1] - source_img.shape[0]
        new_width = source_img.shape[1] - crop
        source_img = source_img[:, 0:new_width]
        return source_img

def match_image_resize(new_tile, square_pixel, source_images):
    img = io.imread(new_tile)
    img = resize(img, (square_pixel,square_pixel), anti_aliasing=True)

    return img

if __name__ == '__main__':
    main()