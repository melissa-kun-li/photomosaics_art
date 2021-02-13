from PIL import Image
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import resize

# TO DO:
# 1. make the pythagoras function/match the average rgbs, return the filename of the matching source image
# 2. resize the matching source image to the size of the square_pixel
#       img = resize(my_image, (square_pixel,square_pixel), anti_aliasing=True)
# 3. paste the image into the location of the pic

def main():
    # LET THE USER SET THIS IN FUTURE
    square_pixel = 50
    # load input image
    my_image = io.imread('doggo.jpg')
    # load source images, future let person decide which dir
    photo_dir= './small_photoset/*jpg'
    # dictionary where the keys are the filenames of the source images, and the values are the loaded source_image
    source_images = {}
    # dictionary where the keys are the filenames of the source images, and the values are the average rgb values
    source_image_avg_rgb_dict = {}
   
    image_collection = io.imread_collection(photo_dir)
    for filepath in image_collection.files:
        filename = filepath
        # filename = filepath[len(photo_dir)-4:]
        source_image = io.imread(filepath)
        # crop to square:
        source_images[filename] = square_source_images(source_image)
        # source_images[filename] = source_image

    # iterate through dictionary, setting img = the loaded image
    for source_image in source_images:
        img = source_images[source_image]
 
        # set the values of the dictionary with the average rgb colour 
        source_image_avg_rgb_dict[filename] = calculate_average_colour(img)

        # print(list(calculate_average_colour(img)))


    trim_rows = my_image.shape[0] % square_pixel
    trim_columns = my_image.shape[1] % square_pixel
    print(my_image.shape)

    my_image = my_image[0:my_image.shape[0]-trim_rows, 0:my_image.shape[1]-trim_columns]
    print(my_image.shape)

    for i in range(0, my_image.shape[0], square_pixel):
        for j in range(0, my_image.shape[1], square_pixel):
            # instead of setting to red, call the function that calculates avg RGB in the square_pixel
            # then call the function that compares the average RGB to the source images
            # then crop the source images into a square and resize to the square_pixel dimensions
            # then replace that part of the original with the "new pixel"
            # done? 

            pixel_region = my_image[i:i+square_pixel, j:j+square_pixel]
            pixel_colour = calculate_average_colour(pixel_region)
            # print(pixel_colour)

            new_tile = match_colour_resize_tile(pixel_colour, source_image_avg_rgb_dict)

            resized_tile = match_image_resize(new_tile, square_pixel)

            # paste the match_colour tile into the square of the original image

            my_image[i:i+square_pixel, j:j+square_pixel] = pixel_colour


    plt.imshow(my_image)
    plt.show()

# list turns [1 2 3] to [1, 2, 3] so that I can match avg rgb colours easier
def calculate_average_colour(pixel_region):
    return(list(np.mean(pixel_region, axis =(0,1))))

# def load_source_images():
#     images = []
#     image_collection = skimage.io.imread_collection('./small_photoset/*jpg')


def match_colour_resize_tile(pixel_colour, source_image_avg_rgb_dict):
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

def match_image_resize(new_tile, square_pixel):
    img = io.imread(new_tile)
    img = resize(img, (square_pixel,square_pixel), anti_aliasing=True)
    return img

if __name__ == '__main__':
    main()