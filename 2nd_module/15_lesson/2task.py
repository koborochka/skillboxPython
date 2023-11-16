import math

class MyMath:
    @staticmethod
    def circle_len(radius: float) -> float:
        return 2 * math.pi * radius

    @staticmethod
    def circle_sq(radius: float) -> float:
        return math.pi * radius**2

    @classmethod
    def cube_volume(cls, side_length: float) -> float:
        return side_length**3

    @classmethod
    def sphere_surface_area(cls, radius: float) -> float:
        return 4 * math.pi * radius**2

res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.cube_volume(side_length=3)
res_4 = MyMath.sphere_surface_area(radius=4)

print(res_1)
print(res_2)
print(res_3)
print(res_4)
