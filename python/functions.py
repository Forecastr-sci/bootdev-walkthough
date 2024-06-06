from typing import Tuple


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


# Write the hours_to_seconds function. It should convert hours to seconds.
def hours_to_seconds(hrs: int) -> int:
    return hrs * 3600


def test_hours_to_seconds():
    assert hours_to_seconds(1) == 3600
    assert hours_to_seconds(10) == 36000
    assert hours_to_seconds(25) == 90000


# Assignment
#
# Complete the become_warrior function. It accepts 3 inputs:
#
#     first_name: string
#     last_name: string
#     power: integer
#
# It should return 2 values:
#
#     The warrior's "title", which is a string in this format:
#
# first_name last_name the warrior
#
# Where first_name and last_name are the actual values of the first_name and last_name inputs. Note: make sure the format is exact, do not add capitalization or punctuation.
#
#     A new "power" value that is equal to the input power plus one.
# I'll be fancy and if I can make an easy one-liner, i'll do lambda functions instead (if it doesn't need testing)
def become_warrior(first_name: str, last_name: str, power: int) -> Tuple[str, int]:
    return f"{first_name} {last_name} the warrior", power + 1


def test_become_warrior():
    assert become_warrior("Ryan", "Gosling", 68) == ("Ryan Gosling the warrior", 69)


def get_punched(health, armor=0):
    DMG = 50
    health -= DMG - armor
    return health


def get_slashed(health, armor=0):
    DMG = 100
    health -= DMG - armor
    return health


def test_attacks():
    # without armor
    assert get_punched(100) == 50
    assert get_slashed(100) == 0
    # with armor
    assert get_punched(100, 30) == 80
    assert get_slashed(100, 70) == 70


def curse(weapon_damage: float) -> Tuple[float]:
    """takes a base damage of a weapon and returns a tuple of floats.
    These floats represent damage with two types of curse applied.
    Lesser curse lowers damage to 50% of the base one.
    Greated curse lowers damage to 25% of the base one."""

    return tuple(weapon_damage * perc for perc in (0.5, 0.25))


def test_curse():
    assert curse(500) == (250, 125)
    assert curse(0) == (0, 0)


def enchant_and_attack(
    target_health: int, damage: int, weapon: str
) -> Tuple[int, int, str]:
    dmg_new = damage + 10
    health_new = target_health - dmg_new
    enchanted_weapon = f"enchanted {weapon}"

    return (enchanted_weapon, health_new)


def test_enchant_and_attack():
    assert enchant_and_attack(70, 20, "spear") == ("enchanted spear", 40)
