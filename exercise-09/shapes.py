from dataclasses import dataclass
import math
from geo import Object2D, Vector2D, GuiWrapper


@dataclass
class Circle(Object2D):
    '''
    Invarianten:
    - radius > 0    
    '''
    __radius: float

    def __post_init__(self):
        assert self.radius > 0, f"Radius {self.radius} muss größer als 0 sein."

        self.__top_left = super().pos - Vector2D(self.radius, self.radius)
        self.__bottom_right = super().pos + \
            Vector2D(self.radius, self.radius)

    @property
    def radius(self) -> float:
        return self.__radius

    @property
    def top_left(self) -> Vector2D:
        return self.__top_left

    @property
    def bottom_right(self) -> Vector2D:
        return self.__bottom_right

    def draw(self, gui, fillcolor="black", outlinecolor="black"):
        gui.canvas.create_oval(self.top_left.x, self.top_left.y, self.bottom_right.x,
                               self.bottom_right.y, fill=fillcolor, outline=outlinecolor)


@dataclass
class RotatableEllipse(Object2D):
    '''
    Invarianten:
    - size.x > 0
    - size.y > 0
    - 0 <= angle < 2 * pi
    '''
    __size: Vector2D
    __angle: float = 0  # Winkel in Bogenmaß

    def __post_init__(self):
        assert self.size.x > 0, f"X-Radius {self.size.x} muss größer als 0 sein."
        assert self.size.y > 0, f"Y-Radius {self.size.y} muss größer als 0 sein."

        assert self.angle >= 0, f"Der Winkel {self.angle} muss größer oder gleich 0 sein."
        assert self.angle < 2 * \
            math.pi, f"Der Winkel {self.angle} muss kleiner 2 * pi sein."

    @property
    def size(self) -> Vector2D:
        return self.__size

    @property
    def angle(self) -> float:
        return self.__angle

    def draw(self, gui, fillcolor="black", outlinecolor="black"):
        points_original = []
        for i in range(360):
            x = self.size.x * math.cos(math.radians(i))
            y = self.size.y * math.sin(math.radians(i))
            points_original += [Vector2D(x, y)]
        points_rotated = []
        # The ellipse is rotated by the negative angle because the y-axis is inverted
        for point in points_original:
            x = point.x * math.cos(-self.angle) - \
                point.y * math.sin(-self.angle)
            y = point.x * math.sin(-self.angle) + \
                point.y * math.cos(-self.angle)
            points_rotated += [Vector2D(x, y)]
        points_transformed = []
        for point in points_rotated:
            points_transformed.append(point.x + self.pos.x)
            points_transformed.append(point.y + self.pos.y)
        gui.canvas.create_polygon(
            *points_transformed, fill=fillcolor, outline=outlinecolor)


@dataclass
class Triangle(Object2D):
    __edge1: Vector2D  # Relative Position des ersten Eckpunktes
    __edge2: Vector2D  # Relative Position des zweiten Eckpunktes

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
