import cv2 as cv
import numpy as np
import os
# net = cv.dnn.readNet('yolov4/yolov4.weights', 'yolov4/yolov4.cfg')
# classes = []
#
# with open("coco.names", "r") as f:
#     classes = [line.strip() for line in f.readlines()]
#
# print(classes)
#
ITEMS_THRESHOLD = 0.80


def verifyItems(fieldimg):
    itemslocations = []
    path = 'training/Items/'
    for file in os.listdir(path):
        if '.jpg' in file:
            itemimg = cv.imread(path+file, cv.IMREAD_UNCHANGED)
            itemimgresized = cv.resize(itemimg, (22,22))
            locationVerify = cv.matchTemplate(fieldimg, itemimgresized, cv.TM_CCOEFF_NORMED)
            locations = np.where(locationVerify >= ITEMS_THRESHOLD)
            print(locations)
            if locations:
                print(file)
            locations = list(zip(*locations[::-1]))
            #print(locations)
            itemslocations.append(locations)
    return itemslocations


fieldimg = cv.imread('screenshots/Base/SharedDraft.jpg', cv.IMREAD_UNCHANGED)
itemslocations = verifyItems(fieldimg)
# jarvanimg = cv.imread('training/Items/ChainVest.jpg', cv.IMREAD_UNCHANGED)
# jarvanimg = cv.resize(jarvanimg, (20,20))
#
#
# print(jarvanimg)
# result = cv.matchTemplate(fieldimg, jarvanimg, cv.TM_CCOEFF_NORMED)
# print(result)
#
# threshold = 0.99
# locations = np.where(result >= threshold)
# locations = list(zip(*locations[::-1]))



#print(locations)

for itemlocation in itemslocations:
    if  itemlocation:
        print(itemlocation)
        print("Found")

        item_w = 22
        item_h = 22
        line_color = (0,255,0)
        line_type = cv.LINE_4

        for loc in itemlocation:
            top_left = loc
            bottom_right = (top_left[0] + item_w, top_left[1] + item_h)

            cv.rectangle(fieldimg, top_left, bottom_right, line_color, thickness=1, lineType=line_type)
            #cv.imwrite('result.jpg', fieldimg)
        cv.imshow('Match', fieldimg)
        cv.waitKey()

    else:
        print('Not found')



