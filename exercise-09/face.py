import math
from geo import Vector2D, GuiWrapper
from shapes import Circle, RotatableEllipse, Triangle


def draw_clown_face():
    gui = GuiWrapper(width=300, height=290)

    hair = RotatableEllipse(Vector2D(150, 70), Vector2D(100, 60), 0)
    face = RotatableEllipse(Vector2D(150, 150), Vector2D(100, 120), 0)
    eye1 = Circle(Vector2D(100, 110), 20)
    eye2 = Circle(Vector2D(200, 110), 20)
    nose = RotatableEllipse(Vector2D(150, 160), Vector2D(15, 30), 0)
    mouth = Triangle(Vector2D(100, 210), Vector2D(
        100, 0), Vector2D(50, 30))
    ear1 = RotatableEllipse(Vector2D(55, 100), Vector2D(10, 20), 7/8*math.pi)
    ear2 = RotatableEllipse(Vector2D(245, 100), Vector2D(10, 20), 1/8*math.pi)
    eyebrow1 = Triangle(Vector2D(75, 80), Vector2D(
        50, -15), Vector2D(50, 0))
    eyebrow2 = Triangle(Vector2D(175, 80), Vector2D(
        50, -15), Vector2D(50, 0))
    iris1 = Circle(Vector2D(105, 115), 10)
    iris2 = Circle(Vector2D(205, 115), 10)
    pupil1 = Circle(Vector2D(105, 115), 2)
    pupil2 = Circle(Vector2D(205, 115), 2)

    hair.draw(gui, fillcolor="red")
    face.draw(gui, fillcolor="white")
    eye1.draw(gui, fillcolor="white")
    eye2.draw(gui, fillcolor="white")
    nose.draw(gui, fillcolor="red")
    mouth.draw(gui, fillcolor="blue")
    ear1.draw(gui, fillcolor="white")
    ear2.draw(gui, fillcolor="white")
    eyebrow1.draw(gui, fillcolor="black")
    eyebrow2.draw(gui, fillcolor="black")
    iris1.draw(gui, fillcolor="green")
    iris2.draw(gui, fillcolor="green")
    pupil1.draw(gui, fillcolor="black")
    pupil2.draw(gui, fillcolor="black")

    gui.start()


if __name__ == "__main__":
    draw_clown_face()
