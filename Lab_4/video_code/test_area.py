""" code will test area.py """

from unittest import TestCase
from area import triangle_area # from the area.py file, import function triangle_area, reduces code

class TestShapeAreas(TestCase):

    def test_triangle_area(self):
        # a triangle with height 4 and base 5 should have an area of 10
        self.assertEqual(10, triangle_area(4,5)) # first argument is exepted, second is actual

    def test_triangle_area_floating_point(self): 
        # a triangle with height 4 and base 5 should have an area of 10
        self.assertAlmostEqual(17.79875, triangle_area(7.25, 4.91)) # assertAlmostEqual will round floating point
    
    #use self.assertRaises("name of error"), use context manager, test will pass only if ValueError is raised
    def test_negative_base_height_raises_value_error(self):
        with self.assertRaises(ValueError):
            triangle_area(-9,2)

        with self.assertRaises(ValueError):
            triangle_area(0,-2)

        with self.assertRaises(ValueError):
            triangle_area(-9,-2)

    def test_zero_value_for_base_height_area(self): 
        # a triangle with height 4 and base 5 should have an area of 10
        self.assertEqual(0, triangle_area(0,5))

        self.assertEqual(0, triangle_area(9,0))

        self.assertEqual(0, triangle_area(0,0))
