import tensorflow as tf
import numpy as np
import cv2
import pathlib

interpreter = tf.lite.Interpreter(model_path="model.tflite")

labels = ['Monnalisa','Urlo di Munch','Notte Stellata','Bacio','Venere','Persistenza','Ragazza con Turbante','Guernica']

interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

for i,od in enumerate(output_details):
    print(i,"\t",od,"\n")


def draw_rect(image, box,detected_class_idx):
    y_min = int(max(1, (box[0] * 320)))
    x_min = int(max(1, (box[1] * 320)))
    y_max = int(min(320, (box[2] * 320)))
    x_max = int(min(320, (box[3] * 320)))
    
    # draw a rectangle on the image
    cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 0, 255), 2)
    cv2.putText(image,labels[int(detected_class_idx)], (x_min,y_min-15),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)

for file in pathlib.Path('images').iterdir():

    if file.suffix != '.jpeg' and file.suffix != '.png' and file.suffix != '.jpg' and file.suffix != '.webp':
        continue
    
    img = cv2.imread(r"{}".format(file.resolve()))
    new_img = cv2.resize(img, (320,320))
    interpreter.set_tensor(input_details[0]['index'], [new_img])

    interpreter.invoke()
    rects = interpreter.get_tensor(
        output_details[1]['index'])

    scores = interpreter.get_tensor(
        output_details[0]['index'])
    
    classes = interpreter.get_tensor(
        output_details[3]['index'])
    print("scores:",scores,"\n")

    print("boxes:",rects,"\n")

    print("classes:",classes)

    print(interpreter.get_tensor(output_details[0]['index']))
    for index, score in enumerate(scores[0]):
        if score > 0.5:
          draw_rect(new_img,rects[0][index],classes[0][index])
          
    cv2.imshow("image", new_img)
    cv2.waitKey(0)