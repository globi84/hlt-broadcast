from PIL import Image, ImageDraw, ImageFont
import textwrap

def textsize(text, font):
    im = Image.new(mode="RGB", size=(0, 0))
    draw = ImageDraw.Draw(im)
    _, _, width, height = draw.textbbox((0, 0), text=text, font=font)
    return width, height

def convert(quote, author, fg, image, border_color, font_file=None, font_size=None, width=520, height=550):
    sentence = f"{author}\n\n{quote}"

    quote_font = ImageFont.truetype(font_file if font_file else "fonts/Coves Bold.otf", font_size if font_size else 32)

    img = Image.open(image, 'r')
    d = ImageDraw.Draw(img)

    wrapped_lines = []
    for line in sentence.split("\n"):  # Erhalte ursprüngliche Zeilenumbrüche
        if line.strip():  # Leere Zeilen beibehalten
            wrapped_lines.extend(textwrap.wrap(line, width=int(width / textsize("A", quote_font)[0] * 1.2)))
        else:
            wrapped_lines.append("")  # Behalte leere Zeilen bei

    wrapped_text = "\n".join(wrapped_lines)

    text_w, text_h = textsize(wrapped_text, quote_font)
    qx = (img.width - text_w) / 2
    qy = (img.height - text_h) / 2

    # Randtext für bessere Lesbarkeit
    for dx, dy in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
        d.text((qx+dx, qy+dy), wrapped_text, align="left", font=quote_font, fill=border_color)

    d.text((qx, qy), wrapped_text, align="left", font=quote_font, fill=fg)

    return img
