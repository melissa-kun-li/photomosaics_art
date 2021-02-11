from PIL import Image
from skimage import io
import numpy as np
import matplotlib.pyplot as plt


# my_image = Image.open('doggo.jpg')
# im.show()
# im.size = (width, length)
# print(im.size) 
# convert image to numpy array
# numpy_array = np.array(im)
# # (height, width)
# print(numpy_array.shape)

def main():
    my_image = io.imread('doggo.jpg')

# image as numpy array
# # (height, width, channel)
# my_image[0:300, 0:200, :] = [255, 0, 0]
# plt.imshow(my_image)
# plt.show()

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
            my_image[i:i+square_pixel, j:j+square_pixel] = [255, 0, 0]

    plt.imshow(my_image)
    plt.show()

if __name__ == '__main__':
    main()

# my_image[0:square_pixel, 0:square_pixel, :] = [255, 0, 0]
# plt.imshow(my_image)
# plt.show()