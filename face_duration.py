import cv2
import dlib
import numpy as np
from scipy.spatial import distance as dist
import json
import argparse

# Initialize argument parser
parser = argparse.ArgumentParser()
parser.add_argument('video', help='path to the input video file')
args = parser.parse_args()

# Initialize dlib's face detector and facial landmarks predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  
facerec = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")  

face_dict = {}

# Open the video file
cap = cv2.VideoCapture(args.video)

frame_rate = cap.get(cv2.CAP_PROP_FPS)
frame_count = 0

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret:
        if frame_count % (30*frame_rate) == 0:
            faces = detector(frame, 1)
            
            for i, face in enumerate(faces):
                shape = predictor(frame, face)
                face_descriptor = facerec.compute_face_descriptor(frame, shape)
                face_descriptor = np.array(face_descriptor)

                for known_face in face_dict.keys():
                    euclidean_distance = dist.euclidean(known_face, face_descriptor)

                    if euclidean_distance < 0.6:
                        face_dict[known_face] += 1/ frame_rate
                        break
                else:
                    face_dict[face_descriptor.tolist()] = 1/ frame_rate

        frame_count += 1

    else:
        break

cap.release()

# Convert the dictionary to JSON and write to a file
with open('face_duration_output.json', 'w') as json_file:
    json.dump(face_dict, json_file)
