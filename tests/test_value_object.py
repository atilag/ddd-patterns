# (C) Copyright Juan Gomez Mosquera 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import unittest

from ddd import ValueObject


class TestValueObject(ValueObject):
    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3


class TestValueObject(unittest.TestCase):
    def setUp(self):
        pass

    def test_value_object_is_inmutable(self):
        self.assertEqual(False, True)

    def test_two_equal_value_objects_are_equal(self):
        self.assertEqual(True, False)

    def test_different_value_objects_are_different(self):
        self.assertEqual(True, False)
