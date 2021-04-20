# (C) Copyright Juan Gomez Mosquera 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import uuid
import pytest
from dataclasses import dataclass
from ddd import Entity


class MyEntity(Entity):
    pass


class TestEntity:
    def test_entity_creates_id(self):
        assert MyEntity(id="123456").id == "123456"

    def test_two_entities_are_equal_if_ids_are_equal(self):
        entity1 = MyEntity(id="12345678")
        entity2 = MyEntity(id="12345678")
        assert entity1 == entity2

    def test_two_entities_are_different_if_ids_are_different(self):
        entity1 = MyEntity()
        entity2 = MyEntity()
        assert entity1 != entity2
