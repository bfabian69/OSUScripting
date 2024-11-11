from PIL import Image

def grayscale(image):
    """Converts the argument image to grayscale."""
    for y in range(image.height):
        for x in range(image.width):
            (r, g, b) = image.getpixel((x, y))
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b
            image.putpixel((x, y), (lum, lum, lum))

def sepia(image):
    """Converts the argument image to sepia tone."""

    grayscale(image)

    for y in range(image.height):
        for x in range(image.width):
            (red, green, blue) = image.getpixel((x, y))

            if red < 63:
                red = int(red * 1.1)
                blue = int(blue * 0.9)
            elif red < 192:
                red = int(red * 1.15)
                blue = int(blue * 0.85)
            else:
                red = min(int(red * 1.08), 255)
                blue = int(blue * 0.93)

            image.putpixel((x, y), (red, green, blue))

if __name__ == "__main__":
    
    image = Image.open("smokey.gif")
    image = image.convert("RGB") 

    sepia(image)

    image.show()

    image.save("smokey_sepia.gif")
