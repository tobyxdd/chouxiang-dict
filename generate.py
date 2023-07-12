from PIL import Image, ImageDraw, ImageFont
import os

LETTERS = '典孝急乐麻批蚌绷盒赢输对退寄创绝秀谔鼠兔神殖友人躺卷润狂图了献忠支洼爆死歇反共中美日韩党雅俗佛草逼冲浪汗包子习毛腊偷傻善编恰哈拉摇晶哥粪钓灵车软硬抄爬原马唉资本我爹爷拳'

FONT = ImageFont.truetype('三极隶书简体.ttf', 650)

os.makedirs('small', exist_ok=True)
os.makedirs('large', exist_ok=True)

i = 0
for letter in LETTERS:
    i += 1
    image = Image.new('RGBA', (1000, 1000), (0, 0, 0, 0))

    draw = ImageDraw.Draw(image)
    draw.ellipse((10, 10, 990, 990), outline='black', fill='white', width=30)
    draw.ellipse((80, 80, 920, 920), outline='black', fill='white', width=60)
    draw.text((500, 410), letter, fill='black', anchor='mm', font=FONT)

    image.resize((100, 100), Image.LANCZOS).save(
        f'small/{i:03d}_{letter}.png')  # for emoji
    image.resize((512, 512), Image.LANCZOS).save(
        f'large/{i:03d}_{letter}.png')  # for sticker
