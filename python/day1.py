import pandas as pd

masses = pd.read_csv('input/2019/day1.txt', header=None)[0].tolist()


def fuel_requirement(mass):
    return max(int(mass / 3) - 2, 0)


def test_fuel_requirement():
    # For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
    assert fuel_requirement(12) == 2

    # For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
    assert fuel_requirement(14) == 2

    # For a mass of 1969, the fuel required is 654.
    assert fuel_requirement(1969) == 654

    # For a mass of 100756, the fuel required is 33583.
    assert fuel_requirement(100756) == 33583

test_fuel_requirement()

total_fuel = sum([fuel_requirement(mass) for mass in masses])
print(total_fuel)

# part 2
def fuel_requirement_recursive(mass):
    fuel = [fuel_requirement(mass)]
    while fuel[-1] > 0:
        fuel.append(fuel_requirement(fuel[-1]))

    return sum(fuel)

def test_fuel_requirement_recursive():

    # A module of mass 14 requires 2 fuel.
    # This fuel requires no further fuel
    # (2 divided by 3 and rounded down is 0, which would call for a negative fuel),
    # so the total fuel required is still just 2.
    assert fuel_requirement_recursive(14) == 2

    # At first, a module of mass 1969 requires 654 fuel.
    # Then, this fuel requires 216 more fuel (654 / 3 - 2).
    # 216 then requires 70 more fuel, which requires 21 fuel,
    # which requires 5 fuel, which requires no further fuel.
    # So, the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
    assert fuel_requirement_recursive(1969) == 966

    # The fuel required by a module of mass 100756 and its fuel is:
    # 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.
    assert fuel_requirement_recursive(100756) == 50346


test_fuel_requirement()

total_fuel = sum([fuel_requirement_recursive(mass) for mass in masses])
print(total_fuel)
