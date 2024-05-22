import time
from MangDang.mini_pupper.display import Display
import os
import subprocess
disp = Display()

#Output Folder Location for video frames
output_folder_path = 'Toothless_Frames'

#Frame extraction command
#ffmpeg -i Toothless_Dancing_Video.mp4 -vf scale=240:240 frame_%04d.png

# Main function
def main(output_folder):
    # Get the list of extracted frames
    frames = sorted(os.listdir(output_folder))

    # Loop through frames and display them
    for frame in frames:
        frame_path = os.path.join(output_folder, frame)
        disp.show_image(frame_path)
        time.sleep(0.033)  # Display each frame for ~33ms (30fps)

if __name__ == '__main__':
    main(output_folder_path)