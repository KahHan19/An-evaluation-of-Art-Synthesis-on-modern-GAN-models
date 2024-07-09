from PIL import Image
import os

def resize_images(rawImg, trainSet, targetsize):
    for filename in os.listdir(rawImg):
        if filename.endswith('.jpg'):
            #Open the image
            with Image.open(rawImg + '/' + filename) as img:
                try:
                    #Resize the image
                    with img.resize(targetsize):

                        try:
                            img = img.convert("RGB")
                            resized_img = img.resize(targetsize)
                            #Save the resized image to the output directory
                            resized_img.save(trainSet + '/' + filename)
                        except:
                            print("file corrupted")
                
                except:
                    print("error")

#Change the rawImg to the unprocessed images path
#Change the trainSet to the images path that you wished to store the processed images
rawImg = 'Other Dataset/nude-painting-nu'
trainSet = 'nu128(2)'

#Change this to the size of the desired size of the image, ensure the image is square shape.
#Recommended sizes: (128,128), (512,512) and (1080,1080)
imgSize = 128

recSize = [128,256,512,1024]
# Check if the size is right
if (imgSize not in recSize):
    print("Size error: Please consider a new image size")
targetsize = (imgSize, imgSize)

# Call the resize_images function with the input directory, output directory, and new size
resize_images(rawImg, trainSet, targetsize)
