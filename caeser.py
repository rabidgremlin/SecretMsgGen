from PIL import Image, ImageDraw, ImageFont

#im = Image.open("lena.pgm")
im = Image.new("RGB",(512,512))

draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=128)
draw.line((0, im.size[1], im.size[0], 0), fill=128)

font = ImageFont.truetype("arial.ttf", 25)

draw.text((10, 25), "world", font=font)


del draw

# write to stdout
im.save("bob.png", "PNG")

import codecs
print(codecs.encode('ABC', 'rot_13'))
print(codecs.encode('NOP', 'rot_13'))
print(codecs.encode('123', 'rot_13'))

from metrics import Metrics

m = Metrics(72)
print("72 points are %f px @72dpi" % m.pt2px(72))
print("25 mm are %f px @72dpi" % m.mm2px(25))

m = Metrics(300)
print("72 points are %f px @300dpi" % m.pt2px(72))
print("25 mm are %f px @300dpi" % m.mm2px(25))

print("point 25mm,25mm is " + str(m.mmpoint2px((25,25))))
