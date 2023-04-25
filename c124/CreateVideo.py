import os
import cv2


path = "PRO-C105-Student-Boilerplate-main/Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)
frame =cv2.imread(images[0])
height,width,channels=frame.shape
print("Height,Width,Channels",height,width,channels)

# sunriseVideo=cv2.VideoWriter("sunrise.mp4",cv2.VideoWriter_fourcc(*"DIVX"),41,(width,height))
# for i in range(count-1,0,-1):
#     frame=cv2.imread(images[i])
#     sunriseVideo.write(frame)
# sunriseVideo.release()
# print("The video is created")

sunsetVideo=cv2.VideoWriter("sunset.mp4",cv2.VideoWriter_fourcc(*"DIVX"),10,(width,height))
for i in range(0, count-1):
    frame=cv2.imread(images[i])
    sunsetVideo.write(frame)
sunsetVideo.release()
print("The video is created")


