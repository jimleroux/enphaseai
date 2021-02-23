import pytest
from enphaseAI.problem1 import find_lines_from_points, find_lines_intersection


def test_find_lines_from_points() -> None:
    p0 = 0., "string_input"
    p1 = 1., 2.5

    # Test for string input
    args = [p0, p1]
    pytest.raises(AssertionError, find_lines_from_points, *args)

    # Test for same points
    args = [p1, p1]
    pytest.raises(AssertionError, find_lines_from_points, *args)

    # Test for int inputs
    p0 = 0, 1
    p1 = 2, 4
    args = [p0, p1]
    pytest.raises(AssertionError, find_lines_from_points, *args)

    p0 = 0., 0.
    p1 = 1., 1.

    a, b = find_lines_from_points(p0, p1)
    assert a == 1., "Slope should be 1"
    assert b == 0., "Intersect should be 0"

    p0 = 0., 0.
    p1 = 1., -1.
    a, b = find_lines_from_points(p0, p1)
    assert a == -1., "Slope should be 1"
    assert b == 0., "Intersect should be 0"


def test_find_lines_intersection() -> None:
    l0 = 0., "string_input"
    l1 = 1., 2.5

    # Test for string input
    args = [l0, l1]
    pytest.raises(AssertionError, find_lines_intersection, *args)

    # Test for same lines
    args = [l1, l1]
    pytest.raises(AssertionError, find_lines_intersection, *args)

    # Test for int inputs
    l0 = 0, 1
    l1 = 2, 4
    args = [l0, l1]
    pytest.raises(AssertionError, find_lines_intersection, *args)

    l0 = 1., 0.
    l1 = -1., 0.
    args = [l0, l1]
    x, y = find_lines_intersection(l0, l1)
    assert x == 0. and y == 0., "The intersection should be the origin"
