from PIL import Image
from skimage import io
import numpy as np
import matplotlib.pyplot as plt

# image as numpy array
# # (height, width, channel)
# my_image[0:300, 0:200, :] = [255, 0, 0]
# plt.imshow(my_image)
# plt.show()

def main():
    my_image = io.imread('doggo.jpg')

    # LOAD THE SOURCE IMAGES
    source_images = ''
    # source_images

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


def match_colour_resize_tile(pixel_colour, source_images):
    # calculates Euclidean distance in rgb colour space
    # gets name of smallest distance image
    # make a copy of the tile, then resize it to the square_pixels size
    # return the name of the resized tile to main()
    pass

def square_source_images():
    # squares off all the source/tile images if not already squared off
    # should happen when the program is run?
    pass


if __name__ == '__main__':
    main()

# my_image[0:square_pixel, 0:square_pixel, :] = [255, 0, 0]
# plt.imshow(my_image)
# plt.show()