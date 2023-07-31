from PIL import Image, ImageDraw, ImageFont
import os

from LETTERS import LETTERS

FONT = ImageFont.truetype('assets/三极隶书简体.ttf', 650)

OUTPUT_DIR = 'dist'
SMALL_SUBDIR = f'{OUTPUT_DIR}/small'
LARGE_SUBDIR = f'{OUTPUT_DIR}/large'

os.makedirs(SMALL_SUBDIR, exist_ok=True)
os.makedirs(LARGE_SUBDIR, exist_ok=True)

def main() -> None:
    i = 0
    for letter in LETTERS:
        i += 1
        image = Image.new('RGBA', (1000, 1000), (0, 0, 0, 0))

        draw = ImageDraw.Draw(image)
        draw.ellipse((10, 10, 990, 990), outline='black', fill='white', width=30)
        draw.ellipse((80, 80, 920, 920), outline='black', fill='white', width=60)
        draw.text((500, 410), letter, fill='black', anchor='mm', font=FONT)

        image.resize((100, 100), Image.LANCZOS).save(
            f'{SMALL_SUBDIR}/{i:03d}_{letter}.png')  # for emoji
        image.resize((512, 512), Image.LANCZOS).save(
            f'{LARGE_SUBDIR}/{i:03d}_{letter}.png')  # for sticker

if __name__ == '__main__':
    main()