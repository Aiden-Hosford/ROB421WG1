import cv2
from PIL import Image
from MangDang.LCD.ST7789 import ST7789

class Display:

    def __init__(self):
        self.disp = ST7789()
        self.disp.begin()

    def show_image(self, image):
        image = Image.fromarray(image)
        image = image.resize((320, 240))
        self.disp.display(image)

    def show_video(self, video_path):
        cap = cv2.VideoCapture(video_path)
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret:
                self.show_image(frame)
            else:
                break
        cap.release()

if __name__ == "__main__":
    disp = Display()
    disp.show_video('path_to_your_video.mp4')