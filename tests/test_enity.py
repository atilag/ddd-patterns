# (C) Copyright Juan Gomez Mosquera 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import pytest
from dataclasses import dataclass
from ddd import Entity


class MyEntity(Entity):
    pass


class TestEntity:
    def test_entity_creates_id(self):
        pass

    def test_two_entities_are_equal_if_ids_are_equal(self):
        pass

    def test_two_entities_are_different_if_ids_are_different(self):
        pass
