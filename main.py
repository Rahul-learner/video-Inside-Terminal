import converter
import sys
import os

video_path = sys.argv[1]

#get the terminal width and height
height = os.get_terminal_size().lines
width = os.get_terminal_size().columns
# convert video to ascii
converter.videoToAscii(video_path, width, height).convert()