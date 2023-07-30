import argparse
import cv2

class FaceDetector:
    def __init__(self, face_cascade_path):
        self.face_cascade = cv2.CascadeClassifier(face_cascade_path)

    def detect_faces(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        return frame

class VideoFileFaceDetector:
    def __init__(self, video_file, face_cascade_path):
        self.video = cv2.VideoCapture(video_file)
        self.face_detector = FaceDetector(face_cascade_path)

    def run(self):
        while True:
            ret, frame = self.video.read()
            if not ret:
                break
            frame = self.face_detector.detect_faces(frame)
            cv2.imshow('Video', frame)
            if cv2.waitKey(1) == ord('q'):
                break
        self.video.release()
        cv2.destroyAllWindows()

class WebcamFaceDetector:
    def __init__(self, face_cascade_path):
        self.video = cv2.VideoCapture(0)
        self.face_detector = FaceDetector(face_cascade_path)

    def run(self):
        while True:
            ret, frame = self.video.read()
            frame = self.face_detector.detect_faces(frame)
            cv2.imshow('Webcam', frame)
            if cv2.waitKey(1) == ord('q'):
                break
        self.video.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--video', help='path to video file')
    parser.add_argument('--webcam', action='store_true', help='use webcam')
    args = parser.parse_args()

    face_cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'

    if args.video:
        video_detector = VideoFileFaceDetector(args.video, face_cascade_path)
        video_detector.run()
    elif args.webcam:
        webcam_detector = WebcamFaceDetector(face_cascade_path)
        webcam_detector.run()
    else:
        print('Please specify --video or --webcam')
