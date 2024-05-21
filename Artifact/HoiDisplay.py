from PIL import Image
from MangDang.LCD.ST7789 import ST7789

class Display:

    def __init__(self):
        self.disp = ST7789()
        self.disp.begin()

    def show_image(self, image_path):
        image = Image.open(image_path)
        image.resize((320, 240))
        self.disp.display(image)

if __name__ == "__main__":
    disp = Display()
    disp.show_image('cropped.jpg')