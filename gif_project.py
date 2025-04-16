#GIF project

#imports
import imageio.v3 as iio

#code
filenames = ['smile_1.png', 'smile_2.png','smile_3.png']
images = [ ]

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('smiles.gif', images, duration = 500, loop = 0)