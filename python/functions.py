# assignment 1: write the area_of_circle function, that will take radius as a parameter
def area_of_circle(radius):
    pi = 3.14
    area = pi * (radius**2)

    return area


def test_area_of_circle():
    assert area_of_circle(1) == 3.14
    assert area_of_circle(5) == 78.5


def triple_attack(first, second, third):
    return sum((first, second, third))


def test_triple_attack():
    assert triple_attack(3, 5, 17) == 25
    assert triple_attack(1, 2, 3) == 6


def to_celsius(f_deg):
    c_deg = 5 / 9 * (f_deg - 32)
    return c_deg


def test_to_celsius():
    assert to_celsius(-40) == -40
