from PIL import Image
import argparse

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def getArgs():
    parse = argparse.ArgumentParser()
    parse.add_argument('-f', '--file')
    parse.add_argument('-o', '--out', type=str, help='out file')
    parse.add_argument('--width', type=int, default=80, help='pic width')
    parse.add_argument('--height', type=int, default=80, help='pic height')
    args = parse.parse_args()
    return vars(args)


def getChar(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    return ascii_char[int((gray/257.0) * length)]


def convertPic():
    args = getArgs()
    file = args['file']
    width = args['width']
    height = args['height']
    out = args['out']

    img = Image.open(file)
    img = img.resize((width, height), Image.NEAREST)
    txt = ''

    print(img.getpixel((25, 25)))
    print(*img.getpixel((25, 25)))
    for i in range(height):
        for j in range(width):
            txt += getChar(*img.getpixel((j, i)))
        txt += '\n'

    print(txt)

    if out:
        with open(out, 'w') as f:
            f.write(txt)
    else:
        with open('output.txt', 'w') as f:
            f.write(txt)


if __name__ == '__main__':
    convertPic()





