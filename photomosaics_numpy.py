from PIL import Image
from skimage import io
import numpy as np
import matplotlib.pyplot as plt

# image as numpy array
# # (height, width, )
# my_image[0:300, 0:200, :] = [255, 0, 0]
# plt.imshow(my_image)
# plt.show()

def main():
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
        filename = filepath[len(photo_dir):]
        source_image = io.imread(filepath)
        # crop to square:
        source_images[filename] = square_source_images(source_image)
        # source_images[filename] = source_image

    # iterate through dictionary, setting img = the loaded image
    for source_image in source_images:
        img = source_images[source_image]
         # set the values of the dictionary with the average rgb colour 
        source_image_avg_rgb_dict[filename] = calculate_average_colour(img)



   

# LET THE USER SET THIS IN FUTURE
    square_pixel = 20

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

            new_tile = match_colour_resize_tile(pixel_colour, source_images)

            # paste the match_colour tile into the square of the original image

            my_image[i:i+square_pixel, j:j+square_pixel] = pixel_colour


    plt.imshow(my_image)
    plt.show()


def calculate_average_colour(pixel_region):
    return(np.mean(pixel_region, axis =(0,1)))

# def load_source_images():
#     images = []
#     image_collection = skimage.io.imread_collection('./small_photoset/*jpg')


def match_colour_resize_tile(pixel_colour, source_images):
    # calculates Euclidean distance in rgb colour space
    # gets name of smallest distance image
    # make a copy of the tile, then resize it to the square_pixels size
    # return the name of the resized tile to main()
    pass


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

if __name__ == '__main__':
    main()

# my_image[0:square_pixel, 0:square_pixel, :] = [255, 0, 0]
# plt.imshow(my_image)
# plt.show()