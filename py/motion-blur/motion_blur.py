from math import sin, cos, exp, pi
from PIL import Image
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Motion Blur Images')
parser.add_argument('-im', type=str, required=True, help='name of in file')
parser.add_argument('-out', type=str, required=True, help='name of out file')
parser.add_argument('-a', type=float, required=False, help='a variable') # TODO
parser.add_argument('-b', type=float, required=False, help='b variable') # TODO

def read_image(filename):
    """ Returns an Image object from a filename of an image """ 
    return Image.open(filename)

def image_to_numpy_arr(image):
    """ Returns a numpy array from an image object as input """
    return np.array(image)

def numpy_arr_to_image(np_array):
    """ Returns an Image object from a numpy array """
    return Image.fromarray(np_array.astype('uint8'))

def motion_blur_filter(u, v, T=1, a=0, b=0.08):
    """ Transfer function for a motion blur filter """
    numerator = sin(pi*(a*u + b*v))
    denominator = pi*(a*u + b*v)
    exponential = complex(cos(pi*(a*u + b*v)),-sin(pi*(a*u + b*v)))
    try:
        return T*(numerator/denominator)*exponential
    except:
        return T*exponential

def motion_blur_image(image_freq, H):
    """ Returns the result of the multiplication between an image's frequency matrix
    and the transfer function H which is the motion blur filter """
    rows = height = len(image_freq)
    cols = width = len(image_freq[0]) 
    dimensions = (height, width)
    motion_blur_image_freq = np.zeros(dimensions, dtype=complex)
    for row in range(rows):
        for col in range(cols):
            motion_blur_image_freq[row][col] = image_freq[row][col]*H(row, col)
    return motion_blur_image_freq
def fft2D(image_spatial):
    """ Returns 2D FFT from a numpy matrix """
    return np.fft.fft2(image_spatial)

def ifft2D(image_freq):
    """ Returns inverse 2D FFT from a numpy matrix """
    return np.fft.ifft2(image_freq)

def real_part_of_complex_image(image_complex):
    """ Returns a matrix of only the real parts of the elements of the input matrix """
    return image_complex.real

def motion_blur_image(filename, outname):
    """ Takes a image's file name and applys a motion blur filter to it 
    and saves it as outname """
    im = read_image(filename)
    im_spatial = image_to_numpy_arr(im)
    im_freq = fft2D(im_spatial)
    im_freq_blurred = motion_blur_image(image_freq=im_freq, H=motion_blur_filter)
    """
    im_spatial_blurred = ifft2D(im_freq_blurred)
    image_spatial_blurred_real = real_part_of_complex_image(im_spatial_blurred)
    blurred_image = numpy_arr_to_image(image_spatial_blurred_real)
    blurred_image.show()
    blurred_image.save(outname)
    """


def main():
    args = parser.parse_args()
    filename = args.im
    outname = args.out
    a, b = args.a, args.b
    motion_blur_image(filename, outname)

if __name__ == '__main__':
	main()

