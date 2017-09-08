import cv2
import numpy as np

prefix_dict = {'West':'V000', 'East':'V001', 'North':'V002'}

direction = 'North'
prefix = prefix_dict[direction]
dataset_list = ['AM02', 'AM05', 'AM09', 'PM02']
corr_list =[]
img = {}

with open('d:\Datasets\KAIST_All_Day\%s Sync.txt'%direction, 'r') as fp:
    for line in fp:
        idx_line = (line.strip().split(','))
        idx_line = map(int, idx_line)

        corr = {}
        corr['AM02'] = int(idx_line[0])
        corr['AM09'] = int(idx_line[1])
        corr['PM02'] = int(idx_line[2])
        corr['AM05'] = int(idx_line[3])

        corr_list.append(corr)

for corr in corr_list:
    print(corr)
    for dataset in dataset_list:
        file_name = 'd:\Datasets\KAIST_All_Day\%s\%s-images[RGB]\%s__I%05d.png' % (dataset, direction, prefix, corr[dataset])
        # print(file_name)
        img[dataset] = cv2.imread(file_name)
        img[dataset] = cv2.resize(img[dataset], (400, 400))
        # cv2.imshow(dataset, img[dataset])

    final_img = np.hstack([img[d] for d in dataset_list])
    cv2.imshow('final_img', final_img)
    cv2.waitKey()