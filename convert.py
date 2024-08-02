import os
import subprocess
import sys


source_folder = sys.argv[2]
output_folder = sys.argv[4]

source_path = os.path.join(os.path.dirname(__file__), source_folder)
output_path = os.path.join(os.path.dirname(__file__), output_folder)

def main():
    if not os.path.exists(output_path):
        os.makedirs(output_path, exist_ok=True)

    for video in os.listdir(source_path):
        if not (os.path.exists(f'./{output_folder}/{video.split(".")[0]}.webm') or os.path.exists(f'./{output_folder}/{video.split(".")[0]}.webp')):
            if video.endswith(".gif"):
                subprocess.run(f'ffmpeg -i ./{source_folder}/{video} -c vp9 -b:v 0 -crf 41 ./{output_folder}/{video.split(".")[0]}.webm')
        else:
            print(f'{video} already exists in the targeted directory!')

    print("Done Converting!")

if __name__ == "__main__":
    main()