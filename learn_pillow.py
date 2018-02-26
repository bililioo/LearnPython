# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter

img = Image.open('test.jpg')

w, h = img.size
print('%s x %s' %(w, h))
img.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
img.save('thumbnail.jpg', 'jpeg')

img2 = img.filter(ImageFilter.BLUR)
img2.save('blur.jpg', 'jpeg')


