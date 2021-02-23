from typing import Tuple


def find_lines_from_points(
    p0: Tuple[float, float],
    p1: Tuple[float, float]
) -> Tuple[float, float]:
    """
    Function calculating the line passing throught a pair of points.

    Args:
        p1 (Tuple[float, float]): First point.
        p2 (Tuple[float, float]): Second point.

    Returns:
        Tuple[float, float]: Returns the parameters of the line (a, b)
    """
    
    x0, y0 = p0
    x1, y1 = p1

    assert isinstance(x0, float), "x0 must be a float"
    assert isinstance(y0, float), "y0 must be a float"
    assert isinstance(x1, float), "x1 must be a float"
    assert isinstance(y1, float), "y1 must be a float"
    assert x0 != x1, "Points must be distinct"
    # We want to find the parameters that satisfies
    # y0 = a * x0 + b and y1 = a * x1 + b
    # We can substract both equations and solve for a

    a = (y1 - y0) / (x1 - x0)

    # Then we can solve for b in one equation, lets say
    # b = y0 - a * x0 = y0 - (y1 - y0) / (x1 - x0) * x0

    b = y0 - a * x0

    return a, b


def find_lines_intersection(
    l0: Tuple[float, float],
    l1: Tuple[float, float]
) -> Tuple[float, float]:
    """
    Function calculating the intersection of 2 lines given their parameters (a, b)

    Args:
        l1 (Tuple[float, float]): Parameters describing the first line.
        l2 (Tuple[float, float]): Parameters describing the second line.

    Returns:
        Tuple[float, float]: Returns the location of the points (x, y)
    """

    a0, b0 = l0
    a1, b1 = l1

    assert isinstance(a0, float), "a0 must be a float"
    assert isinstance(b0, float), "b0 must be a float"
    assert isinstance(a1, float), "a1 must be a float"
    assert isinstance(b1, float), "b1 must be a float"
    assert l0 != l1, "Lines should be distict otherwise there is an infinite number of solutions"

    # We look for the point where a0 * x + b0 = a1 * x + b1
    # We solve for x

    x = - (b1 - b0) / (a1 - a0)

    # Plug into one of the equations

    y = a0 * x + b0

    return x, y


if __name__ == "__main__":
    p0 = (-0.5, 5.0)
    p1 = (6.7, -18.5)

    p2 = (0.5, 5.0)
    p3 = (6.7, 18.5)

    a0, b0 = find_lines_from_points(p0, p1)
    a1, b1 = find_lines_from_points(p2, p3)

    l0 = (a0, b0)
    l1 = (a1, b1)
    
    x, y = find_lines_intersection(l0, l1)
