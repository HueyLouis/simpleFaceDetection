# Face Detection
This Python code uses OpenCV to detect faces in a video file or from a webcam feed. It uses the Haar Cascade classifier to detect faces in each frame of the video.

## Requirements
- Python 3
- OpenCV
- argparse

## Usage
To run the code, use the following command:
```bash
python faceDetection.py --video <path_to_video_file>
```
or
```bash
python faceDetection.py --webcam
```
The **--video** option specifies the path to the video file to be processed. The **--webcam** option uses the default webcam as the video source.

## Implementation
The code defines a **FaceDetector** class that takes the path to the Haar Cascade classifier as input. It uses the **cv2.CascadeClassifier** class to load the classifier and detect faces in each frame of the video.

The **VideoFileFaceDetector** and **WebcamFaceDetector** classes use the **FaceDetector** class to detect faces in a video file or from a webcam feed. They use the **cv2.VideoCapture** class to read frames from the video source and the **cv2.imshow** function to display the frames with the detected faces.

The **argparse** module is used to parse command-line arguments. The **--video** option specifies the path to the video file to be processed, and the **--webcam** option specifies that the default webcam should be used as the video source.

## References
- OpenCV documentation: https://docs.opencv.org/
- argparse documentation: https://docs.python.org/3/library/argparse.html
