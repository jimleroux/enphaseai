from typing import Tuple

import numpy as np


class Plane:
    def __init__(
        self,
        normal: Tuple[float, float, float],
        point: Tuple[float, float, float]
    ) -> None:
        """
        Implementation of a plane object. To instanciate the class you need the normal
        vector to the plane and a point on it.

        Args:
            normal (Tuple[float, float, float]): Normal vector to the plane.
            point (Tuple[float, float, float]): Position of a point on the plane.
        """
        self.normal = np.array(normal) / np.linalg.norm(normal)  # Normalize the vector
        self.point = np.array(point)

    def get_parameters(self) -> Tuple[float, float, float, float]:
        """
        Function which calculates the parameters of the given plane. We know that the plane
        must respect the equation: normal dot (x - point) = 0, where x is any other point
        on the plane. The vector x - point lies in the plane, thus it is perpendicular to
        the normal vector.
        """

        # if we distribute the dot product we get
        # normal dot x - normal dot point = 0
        
        normal_dot_point = np.dot(self.normal, self.point)

        # Rewriting the equation
        # x_normal * x + y_normal * y + z_normal * z - normal dot point = 0
        # We can assign

        a, b, c = tuple(self.normal)
        d = - normal_dot_point

        return a, b, c, d

    def distance_from_plane(
        self,
        p1: Tuple[float, float, float]
    ) -> float:
        # We know one point on the plane by its definition, we can then from a vector
        # pointing from this point to p1.

        point_to_p1 = np.array(p1) - self.point

        # to find the distance we then only have to project this vector on the normal
        distance = np.abs(np.dot(self.normal, point_to_p1))

        return float(distance)


if __name__ == "__main__":
    point = (1., 2., 3.)
    normal = (0., 0., 1.)
    p1 = (1., 2., 6.)

    plane = Plane(normal, point)
    a, b, c, d = plane.get_parameters()
    distance = plane.distance_from_plane(p1)
