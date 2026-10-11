from pathlib import Path
from PIL import Image

path = Path(
    "assets/characters/fox/source/"
    "Orange Fox Pixel Art Walk Cycle Sheet.png"
)

with Image.open(path) as img:
    rgba = img.convert("RGBA")
    alpha = rgba.getchannel("A")

    print(f"Ukuran sheet: {rgba.width} x {rgba.height}")

    # Bagi menjadi empat wilayah horizontal untuk analisis awal.
    row_height = rgba.height // 4

    for row in range(4):
        y0 = row * row_height
        y1 = rgba.height if row == 3 else (row + 1) * row_height

        row_alpha = alpha.crop((0, y0, rgba.width, y1))
        print(
            f"Baris {row + 1}: "
            f"y={y0}..{y1}, "
            f"area berisi piksel={row_alpha.getbbox()}"
        )

    print(
        "\nAnalisis awal selesai. "
        "Batas frame individual belum ditetapkan."
    )
