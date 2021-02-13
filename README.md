# :framed_picture: :art: Photomosaic Art Creator
This program will take in an input image (.jpg) and turn it into a photomosaic (.jpg) where each "pixel" is another image (i.e. source image)! The output/photomosaic will be saved as a new copy within the program directory. Within the program, you can specify how large you want the "pixels" to be i.e. how pixellated the photomosaic is.

**Note**: 

Around 10-20 pixels is a good number if your picture height and width are <= 1000 pixels! When you run the program, it will also output the input image's height and width so you can check and resize if needed. If the program is running for longer than 5 minutes, please consider resizing the image! 

## How to run
### 1. Clone this repository:

```https://github.com/melissa-kun-li/photomosaics_art.git```

### 2. Install dependencies (Within the program directory):

```pip3 install -r requirements.txt```

### 3. Add your input image
Put your input image inside the program directory. Your input image will not be overwritten; a new output image will be created.

### 4. In the directory where it was cloned to, open a terminal and run this command to see the command line arguments help:

```python3 photomosaics_numpy.py -h```

### 5. For example:
If your input image is ```input.jpg``` and your desired output image name is ```output.jpg```, and you'd like your "pixel" images to be a 20x20 pixel square in the input image, you can run this:

```python3 photomosaics_numpy.py 20 input.jpg output.jpg```


### 6. After some time, your output image will be in the program directory (saves as a new .jpg) :) 
