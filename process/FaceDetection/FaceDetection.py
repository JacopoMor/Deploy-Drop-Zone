import numpy as np
# import cv2
# import os
import requests
# from PIL import Image
# from io import BytesIO

# image_path = "rooster.jpg"
# confidence_treshold = 0.5
# proto_name = "deploy.prototxt.txt"
# model_name = "res10_300x300_ssd_iter_140000.caffemodel"
# script_path = os.path.dirname(os.path.realpath(__file__))
# model_info_path = os.path.join(script_path, "kaffe_model")

# def upload_model(proto_file=proto_name, model_name=model_name):
#     proto_path = os.path.join(model_info_path, proto_name)
#     model_path = os.path.join(model_info_path, model_name)

#     print("[INFO] load model")
#     net = cv2.dnn.readNetFromCaffe(proto_path, model_path)
#     return net

# def upload_image (image_path):
#     # load the input image and construct an input blob for the image
#     # by resizing to a fixed 300x300 pixels and then normalizing it
#     image = cv2.imread(image_path)
    
#     blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,
#         (300, 300), (104.0, 177.0, 123.0))
#     return blob, image

# def run_detection(net, image_url, confidence_treshold=0.5, save_path=''):
#     # pass the blob through the network and obtain the detections and
#     response = requests.get(image_url)
#     image = Image.open(BytesIO(response.content))
#     image = np.array(image)
#     blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,
#         (300, 300), (104.0, 177.0, 123.0))
#     print(type(image))
    
#     #blob, image = upload_image(image_path)
#     (h, w) = image.shape[:2]
#     print(h,w)
#     # predictions
#     print("[INFO] computing object detections...")
#     net.setInput(blob)
#     detections = net.forward()

#     # loop over the detections
#     for i in range(0, detections.shape[2]):
#         # extract the confidence (i.e., probability) associated with the
#         # prediction
#         confidence = detections[0, 0, i, 2]
#         # filter out weak detections by ensuring the `confidence` is
#         # greater than the minimum confidence
#         print
#         if confidence > confidence_treshold:
#             # compute the (x, y)-coordinates of the bounding box for the
#             # object
#             box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
#             (startX, startY, endX, endY) = box.astype("int")
    
#             # draw the bounding box of the face along with the associated
#             # probability
#             text = "{:.2f}%".format(confidence * 100)
#             y = startY - 10 if startY - 10 > 10 else startY + 10
#             cv2.rectangle(image, (startX, startY), (endX, endY),
#                 (0, 0, 255), 2)
#             cv2.putText(image, text, (startX, y),
#                 cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
#     if save_path:
#         im = Image.fromarray(image)
#         im.save(save_path)
#     return image

#     def show_image(image):

#         # show the output image
#         cv2.imshow("Output", image)
#         cv2.waitKey(0)

    # def save_image(iamge_name, save_path):
    #     im = Image.fromarray(image)
    #     im.save(save_path)


def save_same_photo(image_url, confidence_treshold=0.5, save_path=''):
#     # pass the blob through the network and obtain the detections and
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    image = np.array(image)
    im.save(save_path)





