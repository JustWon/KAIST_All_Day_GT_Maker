import numpy as np
# import pandas as pd
import cv2

direction = "North"
prefix = "V002"
dataset_list = ['AM02', 'AM05', 'AM09', 'PM02']
idx_list = {'AM02':0, 'AM05':0, 'AM09':0, 'PM02':0}
min_idx = 0
max_idx = 30000
offset = 10

while (True):
    img = {}
    for dataset in dataset_list:
        img[dataset] = cv2.imread('d:\Datasets\KAIST_All_Day\%s\%s-images[RGB]\%s__I%05d.png' % (dataset,direction,prefix,idx_list[dataset]))
        img[dataset] = cv2.resize(img[dataset], (400,400))
        # cv2.imshow(dataset, img[dataset])
        # cv2.waitKey()

    final_img = np.hstack([img[d] for d in dataset_list])
    cv2.imshow('final_img', final_img)
    ch = cv2.waitKey()
    # print(ch)

    if (ch == 119):
        idx_list['AM02'] = min(max_idx, idx_list['AM02'] + offset)
    if (ch == 115):
        idx_list['AM02'] = max(min_idx, idx_list['AM02'] - offset)
    if (ch == 101):
        idx_list['AM05'] = max(min_idx, idx_list['AM05'] + offset)
    if (ch == 100):
        idx_list['AM05'] = max(min_idx, idx_list['AM05'] - offset)
    if (ch == 114):
        idx_list['AM09'] = max(min_idx, idx_list['AM09'] + offset)
    if (ch == 102):
        idx_list['AM09'] = max(min_idx, idx_list['AM09'] - offset)
    if (ch == 116):
        idx_list['PM02'] = max(min_idx, idx_list['PM02'] + offset)
    if (ch == 103):
        idx_list['PM02'] = max(min_idx, idx_list['PM02'] - offset)
    if (ch == 121):
        idx_list['AM02'] = min(max_idx, idx_list['AM02'] + offset)
        idx_list['AM05'] = max(min_idx, idx_list['AM05'] + offset)
        idx_list['AM09'] = max(min_idx, idx_list['AM09'] + offset)
        idx_list['PM02'] = max(min_idx, idx_list['PM02'] + offset)
    if (ch == 104):
        idx_list['AM02'] = max(min_idx, idx_list['AM02'] - offset)
        idx_list['AM05'] = max(min_idx, idx_list['AM05'] - offset)
        idx_list['AM09'] = max(min_idx, idx_list['AM09'] - offset)
        idx_list['PM02'] = max(min_idx, idx_list['PM02'] - offset)
    if (ch == 32):
        print(idx_list)
    if (ch == 113):
        exit()



