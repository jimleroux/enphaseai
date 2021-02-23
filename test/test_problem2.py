import numpy as np
import pytest
from enphaseAI.problem2 import Plane


def test_Plane_init() -> None:
    point = (1., 2., 3.)
    normal = (10., 2., 1.)

    plane = Plane(normal, point)
    assert np.linalg.norm(plane.normal) == 1, "Normal vector not normalized"


def test_Plane_get_parameters() -> None:
    point = (1., 2., 3.)
    normal = (0., 0., 1.)
    plane = Plane(normal, point)

    a, b, c, d = plane.get_parameters()

    assert a == 0 and b == 0, "a and b must be 0 because the plane lies in xy"
    assert c == 1, "c must be 1 because the plane point directly in z"
    assert d == - point[2], "The equation of the plane if z - d = 0"


def test_Plane_distance_from_plane() -> None:
    point = (1., 2., 3.)
    normal = (0., 0., 1.)
    p1 = (1., 2., 6.)
    plane = Plane(normal, point)

    distance = plane.distance_from_plane(p1)

    assert distance == 3., "Distance must be 3"
