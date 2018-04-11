With this project you vill be able to convert a movie into images. 


Requirements : 
You should have installed openCV v3.3.1

You need to have a data and imageCreate folder.



Step 1 : 
Convert the movie into data. 
The algotithm takes a data and each X seconds or x frames, an average color is compute from all the pixel's pixels of the frame. This process is make until the video reach the end, then the values are stored into a file under the "data" folder. The name of the file is the name of the movie given as a parameter. 

Differents files : convert_video_to_data_*
convert_video_to_data_time.py : Convert the video based on time. The frame's mean is saved each X second. The time_between_frame can change this X value.
convert_video_to_data_frame_detail.py : Convert the video based on frame. The frame's mean is saved each X frame. The nbr_between_frame can change this X value. This file gives the feedback of the percentage of the video "converted".
convert_video_to_data_frame_small.py The same as the one above, without the feedback. This makes the script run a bit faster.


How to run the script :
python convert_video_to_data_frame_small.py path_to_the_video
exemple : python convert_video_to_data_frame_small.py /home/you_name/Videos/Avatar.mp4


Step 2 : 
Convert the data into image.
The algotithm takes the values of the file and create the picture. It divide the image into N strips, N the number of records, and each strips is colored with the value of the records.



How to run the script :
python convert_data_to_image.py path_to_the_video
exemple : python convert_data_to_image.py ./data/name_of_the_file
