import numpy as np
import cv2
import time
import json
import sys

# height = 1654
# width = 2339

height = 480
width = 860

name_video = ""
file_type = ""
name_save_data = ""


if len(sys.argv) > 1:
	name_video = sys.argv[1]
	index_file_type = name_video.rfind('.')
	file_type = name_video[index_file_type:]
	name_video = name_video[:index_file_type]
	index_name_file = name_video.rfind('/')
	name_save_data = name_video[index_name_file+1:]

print(name_video + file_type)


if name_video == "":
	print("File not specified")
	exit()

file = open(name_video + file_type , 'r')
data = file.read()


data_json = json.loads(data)

blank_image = np.zeros((height,width,3), np.uint8)


for d in range(len(data_json)):

	my_list = data_json[d]

	red = my_list[0]
	green = my_list[1]
	blue = my_list[2]


	percentage = 1.0*d/len(data_json)
	p_plus1 = 1.0*(d+1)/len(data_json)

	blank_image[:,int(percentage*width):int(p_plus1*width)] = (blue, green, red)


cv2.imwrite("imageCreate/"+name_save_data+".png", blank_image)

