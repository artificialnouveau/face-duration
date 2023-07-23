import requests
import os
from pyunpack import Archive

# The URLs where the models can be downloaded
urls = [
    "http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2",
    "http://dlib.net/files/dlib_face_recognition_resnet_model_v1.dat.bz2"
]

files = [
    "shape_predictor_68_face_landmarks.dat.bz2",
    "dlib_face_recognition_resnet_model_v1.dat.bz2"
]

# Function to download files
def download_file(url):
    response = requests.get(url, stream=True)

    # Check if the request was successful
    if response.status_code == 200:
        # The file name is the last part of the URL
        filename = url.split("/")[-1]

        # Write the content of the request to a file
        with open(filename, "wb") as file:
            file.write(response.content)

        print(f"File {filename} downloaded successfully.")
    else:
        print(f"Failed to download file from {url}.")

# Function to extract files
def extract_file(file):
    Archive(file).extractall(".")
    print(f"File {file} extracted successfully.")

# Check if files exist, if not download and extract them
for file, url in zip(files, urls):
    if not os.path.exists(file):
        download_file(url)
        extract_file(file)
    else:
        print(f"File {file} already exists, skipping download.")
