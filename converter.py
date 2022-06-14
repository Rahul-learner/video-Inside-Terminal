import cv2
import os
import colorama

class videoToAscii:
    def __init__(self, video_path, width=100):
        self.video_path = video_path
        self.width = width
        self.cap = cv2.VideoCapture(video_path)
        self.frame_count = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))
        self.frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.frame_size = (self.frame_width, self.frame_height)

    def get_frame(self, frame_number):
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        ret, frame = self.cap.read()
        return frame

    def convert(self):
        for i in range(0, self.frame_count):
            img_count = str(i)
            frame = self.get_frame(i)
            frame = cv2.resize(frame, (self.width, int(self.width * self.frame_height / self.frame_width)), interpolation=cv2.INTER_AREA)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # convert image to ascii
            asciiChars = ["@", "#", "S", "%", "&", "*", "+", ";", ":", ",", ".", " "]
            characters = "".join([asciiChars[pixel//25] for pixel in frame.flatten()])
            os.system("clear")
            print(characters)
