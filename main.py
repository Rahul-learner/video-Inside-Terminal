import PIL.Image

# ascii characters used to buid the image
asciiChars = ["@", "#", "S", "%", "&", "*", "+", ";", ":", ",", ".", " "]

# resize image according to a new width
def resize_image(image, new_width=100):
    width, height = image.size
    print(image.size)
    ratio = width/height
    new_height = int(new_width * ratio)
    print(new_height)
    print(new_width)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# convert each pixel to grayscale
def convert_to_grayscale(image):
    # convert to grayscale
    return image.convert("L")

# convert pixels to a atring of ascii characters
def convert_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([asciiChars[pixel//25] for pixel in pixels])
    return characters

def main(new_width=100):
    # attempt to open iamge from user-input
    path = input("Enter the path of the image:\n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "is not a valid pathname to an image.")
    
    # convert image to ASCII
    new_image_data = convert_to_ascii(convert_to_grayscale(resize_image(image, new_width)))

    # format
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    # print ASCII image
    #print(ascii_image)

    # save ASCII image
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)

    

# get the width of the terminal in pixels
def get_terminal_width():
    import fcntl, termios, struct
    h, w, hp, wp = struct.unpack('HHHH', fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0)))
    return w

width = get_terminal_width()
main(width)