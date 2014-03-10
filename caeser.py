from PIL import Image, ImageDraw, ImageFont
import codecs
from metrics import Metrics,A4_LANDSCAPE_IN_MM
import sys


msg = str(sys.argv[1]).upper()
file_name = str(sys.argv[2])


m = Metrics(300)

font = ImageFont.truetype("arial.ttf", m.mm2pt(10))
im = Image.new("RGB",m.mmpoint2px(A4_LANDSCAPE_IN_MM),"#ffffff")
draw = ImageDraw.Draw(im)


def draw_letter_rect(x,y,letter):
	draw.rectangle( (m.mmpoint2px((x,y)), m.mmpoint2px((x+12,y+10))),outline="#000000", fill=None)
	textsize = draw.textsize(letter)
	tx = m.mm2px(x+2)
	ty = m.mm2px(y)		
	draw.text((tx,ty), letter, font=font,fill="#000000")
	
def draw_empty_rect(x,y):
	draw.rectangle( (m.mmpoint2px((x,y)), m.mmpoint2px((x+12,y+10))),outline="#000000", fill=None)	
	
xpos = 10	
for c in "ABCDEFGHIJKLM":
	draw_letter_rect(xpos,10,c)
	draw_letter_rect(xpos,20,codecs.encode(c,"rot_13"))
	xpos+=12


print(msg)
print(codecs.encode(msg, 'rot_13'))


coded_msg = codecs.encode(msg, 'rot_13')
msg_words = coded_msg.split()

xpos = 10	
ypos = 50
chars_drawn = 0

for word in msg_words:
	if chars_drawn+len(word) > 22:
		chars_drawn = 0
		ypos+=35
		xpos=10		

	for c in word+" ":
		if (c != " "):   
			draw_letter_rect(xpos,ypos,c)
			draw_empty_rect(xpos,ypos+15)
		xpos+=12
		chars_drawn += 1
		if (chars_drawn > 22):
			chars_drawn = 0
			ypos+=35
			xpos=10


# write to stdout
im.save(file_name, "PNG")
