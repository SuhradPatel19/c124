import cv2
import numpy as np
import tensorflow as tf

video = cv2.VideoCapture(0)

model=tf.keras.models.load_model("c124/keras_model.h5")

# print(model)

while True:
    dummy,frame=video.read()
    
    image=cv2.resize(frame,(224,224))

    testImage=np.array(image,dtype=np.float32)
    # print(testImage)

    testImage=np.expand_dims(testImage,axis=0)
    # print(testImage)

    # normalising the array
    normalisedArray=testImage/255.0
    # print(normalisedArray)

    predication=model.predict(normalisedArray)
    print("prediction: ",predication)

    cv2.imshow("mask detection",frame)

    if cv2.waitKey(1)==32:
        print("closing")
        break

video.release()
cv2.destroyAllWindows() 

