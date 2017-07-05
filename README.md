# ASCII-art
use Python3.x and PIL to transform a img<br>
参数说明<br>
必选参数 file，指定图像文件<br>
可选参数<br>
[-h] <br>
[-o OUTPUT] <br>
[--width WIDTH] <br>
[--height HEIGHT]<br>
[--precision PRECISION]<br>
<br><br>
usage: byte.py [-h] [-o OUTPUT] [--width WIDTH] [--height HEIGHT]<br>
               [--precision PRECISION]<br>
               file<br>

positional arguments:<br>
  file                  图像文件路径<br>

optional arguments:<br>
  -h, --help            show this help message and exit<br>
  -o OUTPUT, --output OUTPUT<br>
                        输出结果到文件<br>
  --width WIDTH<br>
  --height HEIGHT<br>
  --precision PRECISION<br>
                        设置精度,精度越高,图像越细致，默认为1，建议在5以内<br>
