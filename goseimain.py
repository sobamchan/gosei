import click
from PIL import Image


@click.command()
@click.option("-a", type=str, required=True)
@click.option("-b", type=str, required=True)
@click.option("-c", type=click.Choice(["white", "off"]), default="white")
@click.option("-o", type=str, required=True)
def main(a, b, c, o):
    a = Image.open(a)
    b = Image.open(b)

    tgt_size: tuple[int, int] = tuple([a.width // 2, a.height // 2])
    bg_size: tuple[int, int] = tuple(
        [tgt_size[0] + 48 + 48, tgt_size[1] * 2 + 48 + 48 + 28]
    )

    a = a.resize(tgt_size)
    b = b.resize(tgt_size)

    rgb = (244, 240, 224) if c == "off" else (255, 255, 255)
    bg = Image.new("RGB", bg_size, rgb)

    bg.paste(a, (48, 48))
    bg.paste(b, (48, 48 + 28 + tgt_size[1]))

    bg.save(o)
