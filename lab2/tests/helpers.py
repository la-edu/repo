from ..helpers import math
from ..helpers import get_area_by_arc

def test_area_calc_by_diameter():
  expected_diameter = math.pi
  expected_area = math.pi * expected_diameter
  # check that area by diameter calculation is correct
  obtained_area = get_area_by_arc(diameter=expected_diameter)
  assert obtained_area == expected_area

def test_area_calc_by_radius():
  expected_radius = math.pi
  expected_area = math.pi * expected_radius
  # check that area by diameter calculation is correct
  obtained_area = get_area_by_arc(radius=expected_radius)
  assert obtained_area == expected_area
