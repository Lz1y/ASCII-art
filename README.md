# ASCII-art
use Python3.x and PIL to transform a img
参数说明
必选参数 file，指定图像文件
可选参数
[-h] 
[-o OUTPUT] 
[--width WIDTH] 
[--height HEIGHT]
[--precision PRECISION]

usage: byte.py [-h] [-o OUTPUT] [--width WIDTH] [--height HEIGHT]
               [--precision PRECISION]
               file

positional arguments:
  file                  图像文件路径

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        输出结果到文件
  --width WIDTH
  --height HEIGHT
  --precision PRECISION
                        设置精度,精度越高,图像越细致，默认为1，建议在5以内
