from PIL import Image
import cv2
import time
import sys
import os
from ffpyplayer.player import MediaPlayer

video_path = sys.argv[1]

def ascii_image(image):
    image = image.convert('L')
    pixels = image.getdata()

    # replace each pixel with a chartacter from array
    chars = " _.,-=+:;!?0123456789$W#@N" #" _.,-=+:;cba!?0123456789$W#@N" #['@', '#', '$', '%', '^', '&', '*', ':', ';', '.', ',']
    new_pixels = [chars[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)

    print("\r" + new_pixels, end="")




player = MediaPlayer(video_path)
vid = cv2.VideoCapture(video_path)
fps = int(vid.get(cv2.CAP_PROP_FPS))

while True:
    _, frame = vid.read()
    if _:
        audio_frame, val = player.get_frame()
        now = time.time()

        #Do your thing
        #frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        frame = Image.fromarray(frame)
        # terminla size of both windows and linux
        width, height = os.get_terminal_size()
        #
        frame = frame.resize((os.get_terminal_size().columns, os.get_terminal_size().lines))
        ascii_image(frame)

        timeDiff = time.time() - now
        if (timeDiff < 1.0/(fps)):
            time.sleep(1.0/(fps) - timeDiff)

    else:
        break

player.close()
cv2.release()
cv2.destroyAllWindows()
sys.exit(0)