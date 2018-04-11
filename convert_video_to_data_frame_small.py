import numpy as np
import cv2
import time
import datetime

import json

import sys

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



if name_video == "":
	print("File not specified")
	exit()

print("Start time : " + str(datetime.datetime.now().time())[:8])
print("...")

cap = cv2.VideoCapture(name_video + file_type)


tTotal = time.time()

nbr_between_frame = 20

list_mean_images = []


fps = cap.get(cv2.CAP_PROP_FPS)
frameNumbers = cap.get(cv2.CAP_PROP_FRAME_COUNT)

videoLength = frameNumbers / fps

print("Name : " + name_save_data)
print("Video's size : " + str(int(videoLength)))
print("FPS : " + str(round(fps)))

def write_into_file(list_mean_images, name_video):

	data = json.dumps(list_mean_images, sort_keys=True)

	file = open('data/'+name_video+'.txt', 'w')
	file.write(data)
	file.close()


def get_mean_value_image(frame):
	height = len(frame)
	width = len(frame[0])

	red_list = []
	blue_list = []
	green_list = []

	for w in frame[0:][::100]:
		for h in w[0:][::100]:
			red_list.append(h[2])
			green_list.append(h[1])
			blue_list.append(h[0])

	r_mean = np.mean(red_list)
	g_mean = np.mean(green_list)
	b_mean = np.mean(blue_list)

	return (int(r_mean),  int(g_mean), int(b_mean))

size_displayed = False

counter = 0


while(True):
	ret, frame = cap.read()
	

	if not size_displayed:
		size_displayed = True
		print("Resolution : " + str(len(frame[0])) + " * " + str(len(frame)))


	if type(frame) is np.ndarray:
		# cv2.imshow('frame',frame)
		counter += 1
		if counter >= nbr_between_frame:
			list_mean_images.append(get_mean_value_image(frame))
			counter = 0

	else:
		break

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


write_into_file(list_mean_images, "data_frame/" + name_save_data)

print("Nbr frames : " + str(len(list_mean_images)))
print("Total time to create the data : " + str(int(time.time() - tTotal)))

cap.release()
cv2.destroyAllWindows()




