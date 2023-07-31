import os
import svgwrite
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.misc import transform


from LETTERS import LETTERS

FONT_SIZE = 650
FONT_FILE = 'assets/三极隶书简体.ttf'

OUTPUT_DIR = 'dist'
SMALL_SUBDIR = f'{OUTPUT_DIR}/small'
LARGE_SUBDIR = f'{OUTPUT_DIR}/large'

os.makedirs(SMALL_SUBDIR, exist_ok=True)
os.makedirs(LARGE_SUBDIR, exist_ok=True)

CANVAS_SIZE = 1000


def main() -> None:
    i = 0
    font = TTFont(FONT_FILE)
    unitsPerEm = font['head'].unitsPerEm
    ttf2em = transform.Identity.scale(1/unitsPerEm, 1/unitsPerEm)
    svgPerEm = 700
    xform = transform.Identity.translate(
        (1000-svgPerEm)/2, svgPerEm).scale(svgPerEm, -svgPerEm).transform(ttf2em)
    glyphSet = font.getGlyphSet()
    for letter in LETTERS:
        i += 1
        pen = SVGPathPen(glyphSet)
        tpen = TransformPen(pen, xform)
        uni_hex = hex(ord(letter))[2:].upper()
        uni_key = f"uni{uni_hex}"
        glyph = glyphSet[uni_key]
        glyph.draw(tpen)
        pen.closePath()
        path = pen.getCommands()
        
        dwg = svgwrite.Drawing(
            f'{SMALL_SUBDIR}/{i:03d}_{letter}.svg', size=(100, 100))
        dwg.viewbox(0, 0, 1000, 1000)
        dwg.add(dwg.ellipse(center=(500, 500), r=(490, 490),
                stroke='black', fill='white', stroke_width=30))
        dwg.add(dwg.ellipse(center=(500, 500), r=(420, 420),
                stroke='black', fill='white', stroke_width=60))
        dwg.add(dwg.path(d=path, fill='black'))
        dwg.save()

        dwg = svgwrite.Drawing(
            f'{LARGE_SUBDIR}/{i:03d}_{letter}.svg', size=(512, 512))
        dwg.viewbox(0, 0, 1000, 1000)
        dwg.add(dwg.ellipse(center=(500, 500), r=(490, 490),
                stroke='black', fill='white', stroke_width=30))
        dwg.add(dwg.ellipse(center=(500, 500), r=(420, 420),
                stroke='black', fill='white', stroke_width=60))
        dwg.add(dwg.path(d=path, fill='black'))
        dwg.save()


if __name__ == '__main__':
    main()
