# Die pillow-Bibliothek importiert das PIL-Modul (Python Image Library)
from PIL import Image


if __name__ == '__main__':
    # Erstelle ein Bild mit AuflÃ¶sung 800x600 wobei die einzelnen
    # Pixel das HSV-Farbformat verwenden (Hue-Saturation-Value).
    size = (800, 600)
    img = Image.new('HSV', size)

    # Setze die Farbe von jedem Pixel auf rot.
    for x in range(size[0]):
        for y in range(size[1]):
            # Bei Interesse siehe HSV-Farbraum auf Wikipedia.
            # Sie mÃ¼ssen fÃ¼r die Aufgabe nicht verstehen, wieso
            # folgendes Tupel der Farbe Rot entspricht.
            red = (255, 255, 255)
            img.putpixel((x, y), red)

    # Speichere das Bild als JPEG-Datei im aktuellen Verzeichnis.
    # Wir konvertieren das HSV-Farbformat zu RGB (Red-Green-Blue),
    # da JPEG kein HSV unterstÃ¼tzt.
    img.convert('RGB').save('my_red_image.jpg', quality=95)
