import cv2
from PIL import Image
import os
import sys
import time
from ffpyplayer.player import MediaPlayer

#asciiChars = " _.,-=+:;cba!?0123456789$W#@N" " .,:;+*&%$#@" ["@", "#", "S", "%", "&", "*", "+", ";", ":", ",", ".", " "]

video_path = sys.argv[1]

def ascii_image(image):
    image = image
    img = image.resize((os.get_terminal_size().columns, os.get_terminal_size().lines))

    img = img.convert('L')
    pixels = img.getdata()

    # replace each pixel with a chartacter from array
    chars = " _.,-=+:;!?0123456789$W#@N" #" _.,-=+:;cba!?0123456789$W#@N" #['@', '#', '$', '%', '^', '&', '*', ':', ';', '.', ',']
    new_pixels = [chars[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)

    print(new_pixels, end="\n")



cap = cv2.VideoCapture(video_path)
player = MediaPlayer(video_path)
fps = int(cap.get(cv2.CAP_PROP_FPS))
try:
    start_time = time.time()
    start = 0
    end = 0
    while(True):
        start = time.time()
        ret, frame = cap.read()
        audio_frame, val = player.get_frame()
        if ret != True:
            break
        else:
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            frame = Image.fromarray(frame)
            ascii_image(frame)
            time_taken = time.time() - start
            sleep_time =(1 / fps - time_taken)
            if sleep_time > 0:
                time.sleep(sleep_time)
                print("Sleeping for: " + str(sleep_time))
            else:
                print("Wake for: " + str(sleep_time))

            end = time.time()
            frps = 1 / (end - start)
            start = end

            frps = int(frps)
            print("FPS: " + str(frps))
            

    cap.release()
    #print the time it take to run the program
    current_time = (time.time() - start_time)
    print("Time taken to run the program: " + str(current_time / 60) + " minutes")
    #cv2.destroyAllWindows()

except KeyboardInterrupt:
    cap.release()
    cv2.destroyAllWindows()

