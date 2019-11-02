from classification import readTrafficSigns
import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

def main(args):
    trainImages, trainLabels, trainRegions = readTrafficSigns(args.data_path)
    print(len(trainLabels), len(trainImages), len(trainRegions))
    region = [int(x) for x in trainRegions[42]]
    print(trainRegions[42])
    plt.imshow(trainImages[42])
    plt.show()
    ROI = trainImages[42][region[1]:region[3], region[0]:region[2]]
    plt.imshow(ROI)
    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Visualizing GTSRB")
    
    parser.add_argument(
      '--data_path',
      default= "/home/liangchuan/Development/data/gtsrb/GTSRB/Final_Training/Images",
      help= "Folder that contains the traffic sign subfolders"
      )

    args = parser.parse_args()
    main(args)
