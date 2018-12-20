#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('gb18030')
from PIL import Image
from pylab import *
img = Image.open("./img/test.jpg")

'''
    thumbnail() 创建图像的缩略图,参数为宽，高，宽高不能超过原来图像的大小，否则保存为原图像大小，宽高比和原图像一致
'''
img.thumbnail((128, 100))

img.show()
