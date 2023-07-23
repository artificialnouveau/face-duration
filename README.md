# Video Face Duration Calculator

This Python script analyzes a video, registering each unique face detected, and calculates the total duration that each unique face is present in the video. The output is saved as a JSON file.

## Requirements

- OpenCV
- dlib
- numpy
- scipy

Install the required libraries using pip:

```bash
pip install opencv-python-headless dlib scipy numpy
```

Additionally, the script requires two pretrained models from dlib:
- `shape_predictor_68_face_landmarks.dat`
- `dlib_face_recognition_resnet_model_v1.dat`

These models can be downloaded from the dlib models repository: http://dlib.net/files/

## Usage

The script requires the path to the video file as a command line argument.

Run the script as follows:

```bash
python script.py /path/to/video.mp4
```

The script will output a JSON file named 'output.json'. This file contains a dictionary where the keys are the face descriptors (converted to lists) and the values are the total durations that each face was detected in the video.

## Limitations

This script simplifies a lot of aspects: it does not consider that the same face could look different under different lighting conditions and angles, and it does not track faces between frames. For a more accurate solution, a more sophisticated face recognition system, possibly using deep learning, would be required. Also, this code does not include any error checking, and real-world code should include error checking.

