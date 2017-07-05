# -*- coding:utf-8 -*-
#http://www.lz1y.cn
from PIL import Image
import argparse

#命令行输入参数处理
parser = argparse.ArgumentParser()

parser.add_argument('file',help='图像文件路径')     #输入文件
parser.add_argument('-o', '--output',help='输出结果到文件')   #输出文件
parser.add_argument('--width', type = int, default = 80) #输出字符画宽
parser.add_argument('--height', type = int, default = 80) #输出字符画高
parser.add_argument('--precision', type = int, default = 1,help = '\n设置精度,精度越高,图像越细致，默认为1，建议在5以内') #输出精度 (覆盖度)

#获取参数
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output
PRECISION = args.precision

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':

    im = Image.open(IMG)
    im = im.resize((WIDTH*PRECISION,HEIGHT*PRECISION), Image.NEAREST)

    txt = ""

    for i in range(HEIGHT*PRECISION):
        for j in range(WIDTH*PRECISION):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'

    print (txt)

    
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)
