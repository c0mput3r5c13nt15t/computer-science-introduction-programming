from PIL import Image
from mandelbrot_color import color


def mandelbrot(c: complex, m: int) -> int:
    """
    Makes m iterations to determine if c is part of the Mandelbrot set. If so it returns the number of iterations, otherwise m.
    """
    z = 0
    for n in range(m):
        z = z**2 + c

        if abs(z) > 2:
            return n
    return m


def sample(z: complex, w: complex, x: int, y: int, sx: int, sy: int) -> complex:
    """
    Translates the pixel coordinates (x, y) on a plane with size (sx, sy) to a complex number c between z and w.
    """
    real = z.real + (w.real - z.real) * x / sx
    imag = z.imag + (w.imag - z.imag) * y / sy
    return complex(real, imag)


def render_mandelbrot(z: complex, w: complex, sx: int, sy: int, m: int, filename: str) -> None:
    """
    Renders the Mandelbrot set for the complex plane between z and w on an image with size (sx, sy) and saves it as a RGB file. The image is also colored using the color function from mandelbrot_color.py.
    """
    img = Image.new('HSV', (sx, sy))

    for x in range(sx):
        for y in range(sy):
            c = sample(z, w, x, y, sx, sy)
            i = mandelbrot(c, m)
            pixel_color = color(i, m)
            img.putpixel((x, y), pixel_color)

    img.convert('RGB').save(filename, quality=95)


if __name__ == "__main__":
    render_mandelbrot(
        -2 - 1j, 1 + 1j,
        900, 600,
        50,
        'output.jpg')
