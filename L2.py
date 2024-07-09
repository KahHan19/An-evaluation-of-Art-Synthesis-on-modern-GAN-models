import os
import cv2
import numpy as np


# Variables to change
trainingImg = "nyest"#Path to folder containing training images
genArt = cv2.imread("khc73_Code\sample_result.png")#Path to folder containing generated result
imgSize = 128 #Size of each generated image, make sure the sizes are 128,256,512,1024


# Get a list of all image files in the folder
imgFiles = [f for f in os.listdir(trainingImg) if f.endswith(".jpg")]

rec_sizes = [128,256,512,1024]
# Check if the size is right
if (imgSize not in rec_sizes):
    print("Size error: Please consider a new image size")


# Load each image file into a numpy array
def trainNp(imgFiles):
    trainDataset = []
    for imgFile in imgFiles:
        imagePath = os.path.join(trainingImg, imgFile)
        image = cv2.imread(imagePath)
        trainDataset.append(image)
    trainDataset = np.array(trainDataset)
    return trainDataset

#Split the generated artwork into individual images
def splitGen(imgSize, genArt):
    row = genArt.shape[1] // imgSize #Get the number of row
    col = genArt.shape[0] // imgSize #Get the number of column
    genImgs = []
    for i in range(col):
        for j in range(row):
            x1 = j * imgSize
            x2 = x1 + imgSize
            y1 = i * imgSize
            y2 = y1 + imgSize
            genImgs.append(genArt[y1:y2, x1:x2]) #Store up the split image
    return genImgs


print("test0")




def nearestN(imgSize,genArt,imgFiles):
    genImgs = splitGen(imgSize, genArt)
    trainDataset = trainNp(imgFiles)
    distances = np.zeros((len(trainDataset), len(genImgs)))
    for i, training_image in enumerate(trainDataset):
        for j, generated_image in enumerate(genImgs):
            distances[i][j] = np.linalg.norm(training_image-generated_image)
    # Find the index of the top 3 generated images that are most similar to each training image
    top = []
    for i in range(distances.shape[0]):
        closestIn = np.argsort(distances[i])[:2]
        top.append(closestIn)
    # Display the top 3 nearest neighbor images for each training image
    for i, genIm in enumerate(top):
        #open each image from the training set
        training_image = cv2.imread(os.path.join(trainingImg, imgFiles[i]))
        for j, o in enumerate(genIm):
            print("Distance = " + str(distances[j][o]))
            cv2.imshow("Generated Image", genImgs[o])
        cv2.imshow("Training Image", training_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

nearestN(imgSize,genArt,imgFiles)