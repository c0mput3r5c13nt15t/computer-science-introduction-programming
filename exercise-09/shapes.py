from dataclasses import dataclass
import math
from geo import Object2D, Vector2D, GuiWrapper


@dataclass
class Circle(Object2D):
    __radius: int

    @property
    def radius(self) -> int:
        return self.__radius

    def __post_init__(self):
        assert self.radius > 0, f"Radius {self.radius} muss größer als 0 sein."

        self.__top_left = super().pos - Vector2D(self.radius, self.radius)
        self.__bottom_right = super().pos + \
            Vector2D(self.radius, self.radius)

    def draw(self, gui, fillcolor="black", outlinecolor="black"):
        gui.canvas.create_oval(self.__top_left.x, self.__top_left.y, self.__bottom_right.x,
                               self.__bottom_right.y, fill=fillcolor, outline=outlinecolor)


@dataclass
class RotatableEllipse(Object2D):
    __size: Vector2D
    __angle: float = 0  # Winkel in Bogenmaß

    @property
    def size(self) -> Vector2D:
        return self.__size

    @property
    def angle(self) -> float:
        return self.__angle

    def __post_init__(self):
        assert self.size.x > 0, f"X-Radius {self.size.x} muss größer als 0 sein."
        assert self.size.y > 0, f"Y-Radius {self.size.y} muss größer als 0 sein."

        assert self.angle >= 0, f"Der Winkel {self.angle} muss größer oder gleich 0 sein."
        assert self.angle < 2 * \
            math.pi, f"Der Winkel {self.angle} muss kleiner 2 * pi sein."

    def draw(self, gui, fillcolor="black", outlinecolor="black"):
        points_without_rotation = []
        # 360 points that describe the ellipse
        for i in range(360):
            x = self.size.x * math.cos(math.radians(i))
            y = self.size.y * math.sin(math.radians(i))
            points_without_rotation.append(Vector2D(x, y))
        points = []
        for point in points_without_rotation:
            # rotate the points counterclockwise
            x = point.x * math.cos(-self.angle) - \
                point.y * math.sin(-self.angle)
            y = point.x * math.sin(-self.angle) + \
                point.y * math.cos(-self.angle)
            points.append(x + super().pos.x)
            points.append(y + super().pos.y)
        # TODO fix the rotation
        gui.canvas.create_polygon(
            *points, fill=fillcolor, outline=outlinecolor)


@dataclass
class Triangle(Object2D):
    __edge1: Vector2D
    __edge2: Vector2D

    @property
    def edge1(self) -> Vector2D:
        return self.__edge1

    @property
    def edge2(self) -> Vector2D:
        return self.__edge2

    def draw(self, gui: GuiWrapper, fillcolor: str = "black", outlinecolor: str = "black"):
        gui.canvas.create_polygon(self.pos.x, self.pos.y, self.pos.x + self.edge1.x, self.pos.y + self.edge1.y,
                                  self.pos.x + self.edge2.x, self.pos.y + self.edge2.y, fill=fillcolor, outline=outlinecolor)


if __name__ == "__main__":
    gui = GuiWrapper(width=800, height=600)
    circle = Circle(Vector2D(100, 200), 75)
    circle.draw(gui, fillcolor="lightblue")

    ellipse = RotatableEllipse(Vector2D(300, 250), Vector2D(200, 50),
                               7 * math.pi / 5)
    ellipse.draw(gui, fillcolor="pink")

    triangle = Triangle(Vector2D(450, 150), Vector2D(200, 150),
                        Vector2D(100, 350))
    triangle.draw(gui, fillcolor="green", outlinecolor="black")

    gui.start()
