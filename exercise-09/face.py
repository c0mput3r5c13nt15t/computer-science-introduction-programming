from geo import Object2D, Vector2D, GuiWrapper
from shapes import Circle, RotatableEllipse, Triangle


def draw_face():
    gui = GuiWrapper(width=800, height=600)
    # Draw a face with a circle for the head, two circles for the eyes, a
    eye1 = Circle(Vector2D(100, 100), 20)
    eye2 = Circle(Vector2D(200, 100), 20)
    nose = RotatableEllipse(Vector2D(150, 150), Vector2D(20, 40), 0)
    mouth = Triangle(Vector2D(100, 200), Vector2D(
        100, 0), Vector2D(50, 50))
    ear1 = RotatableEllipse(Vector2D(50, 50), Vector2D(20, 40), 0)
    ear2 = RotatableEllipse(Vector2D(250, 50), Vector2D(20, 40), 0)
    eyebrow1 = RotatableEllipse(Vector2D(100, 50), Vector2D(20, 10), 0)
    eyebrow2 = RotatableEllipse(Vector2D(200, 50), Vector2D(20, 10), 0)
    pupil1 = Circle(Vector2D(100, 100), 10)
    pupil2 = Circle(Vector2D(200, 100), 10)

    eye1.draw(gui, fillcolor="white")
    eye2.draw(gui, fillcolor="white")
    nose.draw(gui, fillcolor="red")
    mouth.draw(gui, fillcolor="red")
    ear1.draw(gui, fillcolor="pink")
    ear2.draw(gui, fillcolor="pink")
    eyebrow1.draw(gui, fillcolor="black")
    eyebrow2.draw(gui, fillcolor="black")
    pupil1.draw(gui, fillcolor="black")
    pupil2.draw(gui, fillcolor="black")

    gui.start()


if __name__ == "__main__":
    draw_face()
