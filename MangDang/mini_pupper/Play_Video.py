import time
from MangDang.mini_pupper.display import Display
import os
import subprocess
disp = Display()

#File Path for Video:
video_file_location = 'Toothless_Dancing_Video.mp4'

#Output Folder Location for video frames
output_folder_path = 'Aiden_Video_Frames'

#Frame extraction function
def extract_frames(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    command = [
        'ffmpeg', '-i', video_path, '-vf', 'scale=240:240',
        f'{output_folder}/frame_%04d.png'
    ]
    subprocess.run(command)

# Main function
def main(video_path, output_folder):
    
    # Extract frames from the video
    extract_frames(video_path, output_folder)

    # Get the list of extracted frames
    frames = sorted(os.listdir(output_folder))

    # Loop through frames and display them
    for frame in frames:
        frame_path = os.path.join(output_folder, frame)
        disp.show_image(frame_path)
        time.sleep(0.033)  # Display each frame for ~33ms (30fps)

if __name__ == '__main__':
    main(video_file_location, output_folder_path)