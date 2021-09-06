import sys
import os
import argparse

import cv2
import json

import retinex

# similar behavior as run.py, but writes the images to disk instead of cv2.imshowing 
parser = argparse.ArgumentParser(description='headless retinex')
parser.add_argument('data', default="./data", type=str, help='src dir of images to transform')
parser.add_argument('results', default="./results", type=str, help='src dir of images to transform')
args = parser.parse_args()

data_path = args.data
out_path = args.results

img_list = os.listdir(data_path)
if len(img_list) == 0:
    print 'Data directory is empty.'
    exit()

with open('config.json', 'r') as f:
    config = json.load(f)

for img_name in img_list:
    if img_name == '.gitkeep':
        continue
    print("eval {} {}".format(data_path, img_name))
    img = cv2.imread(os.path.join(data_path, img_name))

    img_msrcr = retinex.MSRCR(
        img,
        config['sigma_list'],
        config['G'],
        config['b'],
        config['alpha'],
        config['beta'],
        config['low_clip'],
        config['high_clip']
    )
   
    img_amsrcr = retinex.automatedMSRCR(
        img,
        config['sigma_list']
    )

    img_msrcp = retinex.MSRCP(
        img,
        config['sigma_list'],
        config['low_clip'],
        config['high_clip']        
    )    

    img_name_base = os.path.splitext(img_name)[0] #  abc.jpg -> abc    

    print("write {} {}".format(out_path, img_name_base))
    cv2.imwrite(os.path.join(out_path, img_name_base + "_original.jpg"), img)
    cv2.imwrite(os.path.join(out_path, img_name_base + "_retinex.jpg"), img_msrcr)
    cv2.imwrite(os.path.join(out_path, img_name_base + "_autoretinex.jpg"), img_amsrcr)
    cv2.imwrite(os.path.join(out_path, img_name_base + "_msrcp.jpg"), img_msrcp)


