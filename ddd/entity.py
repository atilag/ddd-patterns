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


class Entity:
    def __init__(self):
        # uuid4() is random UUID
        self._id = uuid.uuid4()

    @property.getter
    def id(self):
        return self._id
