# -*- coding: utf-8 -*-
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont

from .horoscope import Horoscope
from .meme import Meme


TITLE_FONT = ImageFont.truetype("data/DroidSans.ttf", 128)
FONT = ImageFont.truetype("data/DroidSans.ttf", 32 + 16)


<<<<<<< HEAD
# take a horoscope list
horoscope_list = Horoscope.get_horoscope()
print(horoscope_list['leo'])
# take a meme
# Meme.get()
#
#
# fon = Image.new('RGB', (1080, 1920), color='#FFFFFF')
# font = ImageFont.truetype(r'data\DroidSans.ttf', 140)
# meme = Image.open('meme.png', 'r')
# meme = meme.resize((1000, 1000))
#
# fon.save('fon.jpg')
# story_img = ImageDraw.Draw(fon)
#
# story_img.text((100, 100), horoscope_list['leo'][0], align="left", font=font, fill="#000000")
# fon.paste(meme, (40, 880))
#
# fon.show()
=======
class Picture:
    @staticmethod
    def create(name="pic.png", z="leo"):
        # --- Parse content --- #
        horoscope_list = Horoscope.get_horoscope()
        Meme.get()

        # --- Params --- #
        width, height = 1080, 1920
        memesize = int(width / 100 * 94)
        title = horoscope_list[z][0]
        desc = "\n".join(wrap(horoscope_list[z][1], 41))
        start_height = int(height / 100 * 1)

        back = Image.new("RGBA", (width, 1920), color="#282a36")
        meme = Image.open("meme.png").resize((memesize, memesize))
        draw = ImageDraw.Draw(back)

        # --- Title --- #
        w, h = draw.textsize(title, font=TITLE_FONT)
        draw.text(
            (width//2 - w//2, start_height),
            title, font=TITLE_FONT, fill="#f8f8f2")

        # --- Description --- #
        w1, h1 = draw.multiline_textsize(desc, font=FONT)
        draw.multiline_text(
            (width//2 - w1//2, start_height + h),
            desc, font=FONT, fill="#f8f8f2", align="center")

        back.paste(meme, (int(width / 100 * 3), height - memesize - start_height))
        back.save(name)
>>>>>>> 1be61277d29a406ee86aeffce6017dfaa6f112f2