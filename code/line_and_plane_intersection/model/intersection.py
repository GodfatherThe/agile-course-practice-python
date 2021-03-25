import numpy as np

from typing import Tuple
from copy import deepcopy


class Point3D:
    __slots__ = ['x', 'y', 'z']

    def __init__(self, *obj):
        obj = obj[0] if len(obj) == 1 else obj
        if isinstance(obj, Point3D):
            coordinates = obj.to_tuple()
        elif isinstance(obj, (list, tuple)):
            for item in obj:
                if not isinstance(item, (int, float)):
                    raise TypeError(
                        'Point3D::init - Incorrect elements type. Expected: list[float], tuple[float]')
            coordinates = obj
        else:
            raise TypeError(
                'Point3D::init - Incorrect argument type. Expected: list[float], tuple[float], Point3D')
        self.__make_point(coordinates)

    def to_tuple(self) -> Tuple[float, float, float]:
        return self.x, self.y, self.z

    def __str__(self):
        return 'Point3D [x: {}, y: {}, z: {}]'.format(self.x, self.y, self.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __sub__(self, other):
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __make_point(self, xyz: Tuple[float, float, float]) -> None:
        if len(xyz) != 3:
            raise ValueError('Point3D::__make_point - Point must be in 3D space')
        self.x = xyz[0]
        self.y = xyz[1]
        self.z = xyz[2]


class Plane:
    def __init__(self, p1: Point3D, p2: Point3D, p3: Point3D) -> None:
        if not isinstance(p1, Point3D) or not isinstance(p2, Point3D) or not isinstance(p3, Point3D):
            raise TypeError('Plane::init - Incorrect argument type. Plane is defined by three Point3D')
        if p1 == p2 or p2 == p3 or p3 == p1:
            raise ValueError('Plane::init - Incorrect value. Plane is defined by three different points')
        if Line(p1, p2).point_on_line(p3):
            raise ValueError('Plane::init - Incorrect value. Point should not be on the same line')
        self.p1 = deepcopy(p1)
        self.p2 = deepcopy(p2)
        self.p3 = deepcopy(p3)
        self.abcd = self.__canonical_view()

    def point_on_plane(self, p: Point3D) -> bool:
        a, b, c, d = self.abcd
        return a * p.x + b * p.y + c * p.z + d == 0

    def get_describe(self) -> Tuple[float, float, float, float]:
        return self.abcd

    def __canonical_view(self) -> Tuple[float, float, float, float]:
        v = self.p2 - self.p1
        w = self.p3 - self.p1
        d1 = v.y * w.z - v.z * w.y
        d2 = v.x * w.z - v.z * w.x
        d3 = v.x * w.y - v.y * w.x
        return d1, -d2, d3, -self.p1.x * d1 + self.p1.y * d2 - self.p1.z * d3


class Line:
    def __init__(self, p1: Point3D, p2: Point3D) -> None:
        if not isinstance(p1, Point3D) or not isinstance(p2, Point3D):
            raise TypeError('Line::init - Incorrect argument type. Line is defined by two Point3D')
        if p1 == p2:
            raise ValueError('Line::init - Incorrect value. Line is defined by two different points')
        self.p1 = deepcopy(p1)
        self.p2 = deepcopy(p2)
        self.direction = self.__direction()

    def point_on_line(self, p: Point3D) -> bool:
        if self.direction.x == 0 and p.x != self.p1.x:
            return False
        if self.direction.y == 0 and p.y != self.p1.y:
            return False
        if self.direction.z == 0 and p.z != self.p1.z:
            return False
        first_fraction = (p.x - self.p1.x) / self.direction.x if self.direction.x != 0 else 0
        second_fraction = (p.y - self.p1.y) / self.direction.y if self.direction.y != 0 else 0
        third_fraction = (p.z - self.p1.z) / self.direction.z if self.direction.z != 0 else 0
        return (first_fraction == second_fraction) and (second_fraction == third_fraction)

    def get_describe(self) -> Tuple[Point3D, Point3D]:
        return self.p1, self.direction

    def __direction(self) -> Point3D:
        return self.p2 - self.p1


class Intersection:
    @staticmethod
    def have_intersection(line: Line, plane: Plane) -> bool:
        line_point, line_direction = line.get_describe()
        plane_abcd = plane.get_describe()
        plane_normal = plane_abcd[:3]
        is_parallel = np.dot(line_direction.to_tuple(), plane_normal) == 0

        if not is_parallel:
            return True
        else:
            if plane.point_on_plane(line_point):
                return True
            else:
                return False
