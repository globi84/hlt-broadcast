import sys
from PIL import Image, ImageDraw, ImageFont

# load image
img = Image.open('image\\background-template.png')
d1 = ImageDraw.Draw(img)

# load font
myFont = ImageFont.truetype('tahoma.ttf', 27)

text = '''Ja, fest wie die Berge und Felsen,

So stark sei auch unser Stand

auf dem Fels, den unsre Väter

sich schufen durch Gottes Hand;

ja, der Fels unsrer Ehre und Tugend

und des Glaubens an Gott, der lebt.

Der Arm ist stark, unverrückbar,

der stolz das Banner hebt!

Und wir hörn die Erde singen:

Geh voran, geh voran, geh voran!

Berg’ und Täler widerklingen:

Geh voran, geh voran, geh voran!

Strebet nach Recht und nach Tugend,

ein herrlicher Tag bricht an,

drum vorwärts, er siegt die Jugend,

Geh voran, geh voran, geh voran!
'''
# place text
d1.text((1280, 30), text, fill =(255, 255, 255),font=myFont)
#d1.textbbox((30, 780), text, font=myFont)

# save image
img.save('Lieder\\lied.png')
