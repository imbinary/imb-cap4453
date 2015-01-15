__author__ = 'William Orem'

import argparse
import math

# variables
pic = [[0 for x in range(256)] for x in range(256)]
outpicx = [[0 for x in range(256)] for x in range(256)]
outpicy = [[0 for x in range(256)] for x in range(256)]
maskx = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
masky = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]
ival = [[0 for x in range(256)] for x in range(256)]
mr = 1

# parse and load
ap = argparse.ArgumentParser()
ap.add_argument("-i1", "--input1", required=True, help="Path to the image")
# ap.add_argument("-i2", "--input2", required=True, help="Path to the image2")
ap.add_argument("-t", "--threshold", required=True, help="threshold")
ap.add_argument("-o", "--output", required=False, help="Path to the output image")
args = vars(ap.parse_args())
fp1 = open(args["input1"], "r")
# fp2 = open(args["input2"], "r")
# fp3 = open(args["output"], "w")

for i in range(256):
    for j in range(256):
        pic[i][j] = ord(fp1.read(1))

maxival = 0
for i in range(mr, 256-mr):
    for j in range(mr, 256-mr):
        sum1 = 0
        sum2 = 0
        for p in range(-mr, mr):
            for q in range(-mr, mr):
                sum1 += pic[i+p][j+q] * maskx[p+mr][q+mr]
                sum2 += pic[i+p][j+q] * masky[p+mr][q+mr]
        outpicx[i][j] = sum1
        outpicy[i][j] = sum2
        ival[i][j] = math.sqrt(math.pow(outpicx[i][j], 2) + math.pow(outpicy[i][j], 2))
        if ival[i][j] > maxival:
            maxival = ival[i][j]


for i in range(256):
    for j in range(256):
        ival[i][j] = (ival[i][j] / maxival) * 255
        # print ival[i][j]
