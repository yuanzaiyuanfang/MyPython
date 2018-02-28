# -*- coding: utf-8 -*-
"""
__title__ = 'todo'
__author__ = 'MLRC-iOS-CI'
__mtime__ = '2018/2/28'
"""

import argparse
import os
from PIL import Image

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`'. ")
# ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`'. ")
ascii_length = len(ascii_char)

parser = argparse.ArgumentParser()
parser.add_argument('--file', default='ascii_dora.png')  # --可选 d默认值
parser.add_argument('-o', '--output')  # -简写
parser.add_argument('--width', type=int, default=60)  # 输出字符画宽
parser.add_argument('--height', type=int, default=60)  # 输出字符画高
args = parser.parse_args()
IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output


def get_char(r, g, b, alpha=256):
	if alpha == 0:
		return ' '
	gray = 0.2126 * r + 0.7152 * g + 0.0722 * b  # 根据rgb计算灰度
	c = ascii_length / (256.0 + 1) * gray
	return ascii_char[int(c)]  # 根据灰度返回字符


if __name__ == '__main__':
	image = Image.open(IMG)
	(x, y) = image.size
	print('原尺寸 宽：%s，高：%s' % (x, y))
	h = int(y / x * WIDTH)
	image = image.resize((WIDTH, h), Image.NEAREST)
	print('现尺寸 宽：%s，高：%s' % (WIDTH, h))
	txt = ''
	for i in range(h):
		for j in range(WIDTH):
			txt += get_char(*image.getpixel((j, i)))
		txt += '\n'

	if OUTPUT:
		with open(OUTPUT, 'w') as f:
			f.write(txt)
	else:
		with open(os.path.splitext(IMG)[0] + '.txt', 'w') as f:
			f.write(txt)
