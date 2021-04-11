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
from dataclasses import dataclass
from ddd import ValueObject, ValueObjectInmutableError


@dataclass(frozen=True, eq=False)
class MyValueObject(ValueObject):
    field1: str
    field2: int
    field3: dict


class TestValueObject(unittest.TestCase):
    def setUp(self):
        pass

    def test_two_equal_value_objects_are_equal(self):
        obj1 = MyValueObject(1, "2", {"3": "4"})
        obj2 = MyValueObject(1, "2", {"3": "4"})
        self.assertEqual(obj1, obj2)

    def test_different_value_objects_are_different(self):
        obj1 = MyValueObject(1, "2", {"3": "4"})
        obj2 = MyValueObject(2, "2", {"3": "4"})
        self.assertNotEqual(obj1, obj2)
