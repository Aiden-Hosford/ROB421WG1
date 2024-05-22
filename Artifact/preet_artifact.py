from MangDang.LCD.ST7789 import ST7789
import time
from PIL import Image, ImageDraw, ImageFont





if __name__ == "__main__":
    disp = ST7789()
    disp.begin()
    starttime = time.monotonic()
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 48)

    with Image.new("RGB", size=(320, 240)) as im:
        while True:
            currenttime = time.monotonic()
            draw = ImageDraw.Draw(im)
            draw.text(xy=(140, 100), align="center", font=font, text=f"{currenttime-starttime:.2f}")

            # write to stdout
            disp.display(im)
            im.paste((0,0,0), (0,0,320,240))
            time.sleep(0.05 - ((currenttime - starttime) % 0.05))

    

